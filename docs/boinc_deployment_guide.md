# Deploying the AVE Framework to BOINC
**Project Goal:** Analytically derive the Fine-Structure Constant ($\alpha = 1/137.035999$) by finding the topological Rigidity Percolation Threshold ($p_c$) of a 1-Billion Node Amorphous Chiral LC Network.

## 1. The Distributed Architecture (Why BOINC?)
A 1-billion node 3D network requires analyzing a $3 \times 10^9$ rank sparse matrix to identify the exact phase-transition locking point. This requires terabytes of RAM, impossible on a single consumer machine. 

BOINC (Berkeley Open Infrastructure for Network Computing) allows you to break this colossal 3D volume into millions of smaller overlapping 3D chunks (Workunits). The global network of volunteers computes the rigidity tensor of these chunks and returns the data, allowing the master server to stitch together the macroscopic phase transition.

## 2. Core Components Required
To launch "AVE@Home" (or whatever you name the public project), you require three pieces of infrastructure:

### A. The BOINC Master Server
You need a dedicated Linux server (e.g., an AWS EC2 instance or a DigitalOcean Droplet) to act as the project host.
1.  **Install the BOINC Server OS:** Follow the official BOINC server deployment guide to install the database, Apache web server, and BOINC daemons.
2.  **Workunit Generator (Daemon):** A Python or C++ script running on your server that mathematically slices the 1-billion node theoretical 3D bounding box into 1-million node chunks. It generates a `.xml` input file for each chunk detailing its coordinates.
3.  **Validator & Assimilator:** Server-side daemons that check returned user data for errors (Validators) and stitch the returned matrix tensors back into the master dataset (Assimilators).

### B. The C++ Scientific Application (The Client)
This is the program the volunteers actually download and run.
1.  **The Engine:** Expand the `scripts/boinc_alpha_derivation.cpp` file. It must be compiled against the BOINC API C++ libraries (`<boinc_api.h>`).
2.  **The Algorithm:** The core must use a hyper-optimized 3D integer algorithm called the **Pebble Game**. This algorithm calculates network rigidity without floating-point matrices, saving massive amounts of memory.
3.  **Compilation:** You must cross-compile this C++ application for Windows (.exe), Linux, and macOS (Apple Silicon & Intel) so that anyone who volunteers can run it.

### C. The Public Facing Web Portal
This is where volunteers sign up, download the BOINC client, and track their compute credits. The BOINC server software comes with a default PHP web template. You will customize this to explain the physics of the AVE Framework and the goal of deriving $1/137.036$.

## 3. The Execution Pipeline
1.  **Generate:** Your server generates 10,000 workunits, each representing a $100 \times 100 \times 100$ coordinate volume.
2.  **Distribute:** A volunteer's PC requests work. The server sends them the C++ executable and one `.xml` coordinate chunk.
3.  **Compute:** The volunteer's CPU runs the 3D Pebble Game, finding the exact coordination number ($z$) where that specific chunk locks into a rigid solid.
4.  **Return:** The PC uploads the phase-transition state back to your server.
5.  **Assimilate:** Your server maps the returned macroscopic rigidity tensor. As millions of chunks are completed, the global phase transition of the $10^9$ node universe is revealed.

## 4. Next Steps for the Researcher
If you are ready to formally commit to this path:
1.  Spin up an Ubuntu 22.04 LTS server.
2.  Follow the [BOINC Server Creation Guide](https://boinc.berkeley.edu/trac/wiki/ProjectMain).
3.  We will need to fully implement the 3D Pebble Game algorithm in standard C++ to replace the placeholder in `boinc_alpha_derivation.cpp`.
