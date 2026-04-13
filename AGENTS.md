# AGENTS.md

ato is a declarative DSL to design electronics (PCBs) with.
It is part of the atopile project.
Atopile is run by the vscode/cursor/windsurf extension.
The CLI (which is invoked by the extension) actually builds the project.

# Not available in ato

- if statements
- while loops
- functions (calls or definitions)
- classes
- objects
- exceptions
- generators


# Ato Syntax

ato sytax is heavily inspired by Python, but fully declarative.
ato thus has no procedural code, and no side effects.

## Examples of syntax
```ato
#pragma experiment("FOR_LOOP")       # Enable experimental features
from "path/to/source.ato" import SpecificModule
import ModuleName

component MyComponent:
    pin p1

interface MyInterface:
    pin io

module DemoModule from AnotherBaseModule:
    # Declarations and Assignments
    signal my_signal
    a_field: AnotherBaseModule
    voltage: V = 5V
    resistance: ohm = 10kohm +/- 10%
    
    # Assertions
    assert voltage within 3V to 5V
    
    # Instantiations
    instance = new MyComponent
    container = new MyComponent[10]
    templated = new MyComponent<int_=1>
    
    # Connections
    p1 ~ my_signal                       # Standard connection
    instance ~> container[0]             # Bridge connection
    
    # Loops
    for item in container:
        item ~ p1
```

# Most used library modules/interfaces (api of them)

```ato
interface Electrical:
    pass

interface ElectricPower:
    hv = new Electrical
    lv = new Electrical

module Resistor:
    resistance: ohm
    max_power: W
    max_voltage: V
    unnamed = new Electrical[2]

module Capacitor:
    capacitance: F
    max_voltage: V
    unnamed = new Electrical[2]

interface I2C:
    scl = new ElectricLogic
    sda = new ElectricLogic
    frequency: Hz
    address: dimensionless

interface ElectricLogic:
    line = new Electrical
    reference = new ElectricPower
```

For the rest use the atopile MCP server 
- `get_library_interfaces` to list interfaces
- `get_library_modules` to list modules
- `inspect_library_module_or_interface` to inspect the code

# Ato language features

## experimental features

Enable with `#pragma experiment("BRIDGE_CONNECT")`
BRIDGE_CONNECT: enables `p1 ~> resistor ~> p2` syntax
FOR_LOOP: enables `for item in container: pass` syntax
TRAITS: enables `trait trait_name` syntax
MODULE_TEMPLATING: enables `new MyComponent<param=literal>` syntax

## modules, interfaces, parameters, traits

A block is either a module, interface or component.
Components are just modules for code-as-data.
Interfaces describe a connectable interface (e.g Electrical, ElectricPower, I2C, etc).
A module is a block that can be instantiated.
Think of it as the ato equivalent of a class.
Parameters are variables for numbers and they work with constraints.
E.g `resistance: ohm` is a parameter.
Constrain with `assert resistance within 10kohm +/- 10%`.
It's very important to use toleranced values for parameters.
If you constrain a resistor.resistance to 10kohm there won't be a single part found because that's a tolerance of 0%.

Traits mark a module to have some kind of functionality that can be used in other modules.
E.g `trait has_designator_prefix` is the way to mark a module to have a specific designator prefix that will be used in the designator field in the footprint.

## connecting

You can only connect interfaces of the same type.
`resistor0.unnamed[0] ~ resistor0.unnamed[0]` is the way to connect two resistors in series.
If a module has the `can_bridge` trait you can use the sperm operator `~>` to bridge the module.
`led.anode ~> resistor ~> power.hv` connects the anode in series with the resistor and then the resistor in series with the high voltage power supply.

## for loop syntax

`for item in container: pass` is the way to iterate over a container.

# Ato CLI

## How to run

You run ato commands through the MCP tool.

## Packages

Packages can be found on the ato registry.
To install a package you need to run `ato add <PACKAGE_NAME>`.
e.g `ato install atopile/addressable-leds`
And then can be imported with `from "atopile/addressable-leds/sk6805-ec20.ato" import SK6805_EC20_driver`.
And used like this:

```ato
module MyModule:
    led = new SK6805_EC20_driver
```

## Footprints & Part picking

Footprint selection is done through the part choice (`ato create part` auto-generates ato code for the part).
The `pin` keyword is used to build footprint pinmaps so avoid using it outside of `component` blocks.
Preferrably use `Electrical` interface for electrical interfaces.
A lot of times it's actually `ElectricLogic` for things like GPIOs etc or `ElectricPower` for power supplies.

Passive modules (Resistors, Capacitors) are picked automatically by the constraints on their parameters.
To constrain the package do e.g `package = "0402"`.
To explictly pick a part for a module use `lcsc = "<LCSC_PART_NUMBER>"`.


# Creating a package

Package generation process:

Review structure of other pacakges.

1. Create new Directory in 'packages/packages' with naming convention '<vendor>-<device>' eg 'adi-adau145x'
2. create an ato.yaml file in the new directory with the following content:

```yaml
requires-atopile: '^0.9.0'

paths:
    src: '.'
    layout: ./layouts

builds:
    default:
        entry: <device>.ato:<device>_driver
    example:
        entry: <device>.ato:Example
```

3. Create part using tool call 'search_and_install_jlcpcb_part'
4. Import the part into the <device>.ato file
5. Read the datasheet for the device
6. Find common interfaces in the part eg I2C, I2S, SPI, Power

7. Create interfaces and connect them

power interfaces:
power*<name> = new ElectricPower
power*<name>.required = True # If critical to the device
assert power\*<name>.voltage within <minimum*operating_voltage>V to <maximum_operating_voltage>V
power*<name>.vcc ~ <device>.<vcc pin>
power\_<name>.gnd ~ <device>.<gnd pin>

i2c interfaces:
i2c = new I2C
i2c.scl.line ~ <device>.<i2c scl pin>
i2c.sda.line ~ <device>.<i2c sda pin>

spi interfaces:
spi = new SPI
spi.sclk.line ~ <device>.<spi sclk pin>
spi.mosi.line ~ <device>.<spi mosi pin>
spi.miso.line ~ <device>.<spi miso pin>

8. Add decoupling capacitors

looking at the datasheet, determine the required decoupling capacitors

eg: 2x 100nF 0402:

power_3v3 = new ElectricPower

# Decoupling power_3v3

power_3v3_caps = new Capacitor[2]
for capacitor in power_3v3_caps:
capacitor.capacitance = 100nF +/- 20%
capacitor.package = "0402"
power_3v3.hv ~> capacitor ~> power_3v3.lv

9. If device has pin configurable i2c addresses

If format is: <n x fixed address bits><m x pin configured address bits>
use addressor module:

- Use `Addressor<address_bits=N>` where **N = number of address pins**.
- Connect each `address_lines[i].line` to the corresponding pin, and its `.reference` to a local power rail.
- Set `addressor.base` to the lowest possible address and `assert addressor.address is i2c.address`.

10. Create a README.md

# <Manufacturer> <Manufacturer part number> <Short description>

## Usage

```ato
<copy in example>

```

## Contributing

Contributions to this package are welcome via pull requests on the GitHub repository.

## License

This atopile package is provided under the [MIT License](https://opensource.org/license/mit/).

11. Connect high level interfaces directly in example:

eg:

i2c = new I2C
power = new ElectricPower
sensor = new Sensor

i2c ~ sensor.i2c
power ~ sensor.power_3v3

# Additional Notes & Gotchas (generic)

- Multi-rail devices (VDD / VDDIO, AVDD / DVDD, etc.)

    - Model separate `ElectricPower` interfaces for each rail (e.g. `power_core`, `power_io`).
    - Mark each `.required = True` if the device cannot function without it, and add voltage assertions per datasheet.

- Optional interfaces (SPI vs I²C)

    - If the device supports multiple buses, pick one for the initial driver. Leave unused bus pins as `ElectricLogic` lines or expose a second interface module later.

- Decoupling guidance

    - If the datasheet shows multiple caps, model the **minimum required** set so the build passes; you can refine values/packages later.

- File / directory layout recap
    - `<vendor>-<device>/` – package root
    - `ato.yaml` – build manifest (include `default` **and** `example` targets)
    - `<device>.ato` – driver + optional example module
    - `parts/<MANUFACTURER_PARTNO>/` – atomic part + footprint/symbol/step files

These tips should prevent common "footprint not found", "pin X missing", and build-time path errors when you add new devices.


# Vibe coding a project

If the user gives you high level description of the project, use the following guide:

# How LLMs can design electronics:

#1 Rule: USE THE TOOLS. If the tools dont work, dont freak out, you are probably using them wrong. Ask for help if you get stuck.

Top level design

1. Research available packages relevant to the user requests using 'find_packages'
2. Inspect promising packages using 'inspect_package'
3. Propose packages to use for project and architucture to user, revise if needed
4. Install needed packages using 'install_package'
5. Import packages into main file
6. Create instances of packages in main module

## Power

1. Review for each package the required voltage and current (current may not be provided, use judement if nessesary)
2. Determine the power rails that need to be generated and a suitable tollerance (typically ~3-5% is acceptable)
3. Determine the input power source, typically a battery, USB connector or other power connector (eg XT30) and install relevant package
4. Find suitable regulators:
   a) if input voltage > required voltage and current is low, use an LDO package
   b) if input voltage > required voltage and current is high, use buck converter
   c) if input votlage < required voltage, use a boost converter
   d) if input voltage can be both less than or greater than input voltage, use buck boost (eg battery powered device that needs 3v3)
5. If battery powered, add charger package

Typical power architucture example with LDO:

- USB input power
- Low current output (eg microcontroller)

from "atopile/ti-tlv75901/ti-tlv75901.ato" import TLV75901_driver
from "atopile/usb-connectors/usb-connectors.ato" import USBCConn

module App:

    # Rails
    power_5v = new Power
    power_3v3 = new Power

    # Components
    ldo = new TLV75901_driver
    usb_connector = new USBCConn

    # Connections
    usb_connector.power ~ power_vbus
    power_vbus ~> ldo ~> power_3v3

## Communicaions

1. Review packages required interfaces, typically i2c, spi or ElectricLogics
2. Find suitable pins on the controller, typically a microcontroller or Linux SOC
3. Connect interfaces eg micro.i2c[0] ~ sensor.i2c

## Development process notes

- After making changes, be sure to use 'build_project' to update the PCB
- Builds will often generate errors/warnings, these should be reviewed and fixed
- Prioritize pacakges from 'atopile' over other packages
