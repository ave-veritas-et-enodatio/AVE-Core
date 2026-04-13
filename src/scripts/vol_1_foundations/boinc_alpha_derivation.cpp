/**
 * AVE Framework: BOINC Distributed Alpha Derivation Client
 *
 * Objective: To analytically derive the Fine-Structure Constant (1/137.035999)
 * by finding the exact Rigidity Percolation threshold (p_c) of a 3D Amorphous
 * Chiral LC Network using the 3D (3,6) Pebble Game algorithm.
 */

#include <algorithm>
#include <chrono>
#include <cmath>
#include <fstream> // Added for file output
#include <iostream>
#include <queue>
#include <random>
#include <string>
#include <vector>

// BOINC Application API
#include "boinc_api.h"

struct Node3D {
  double x, y, z;
};

class PebbleGame3D {
private:
  int num_nodes;
  std::vector<Node3D> lattice;
  std::vector<int> pebbles;
  std::vector<std::vector<int>>
      directed_edges; // directed graph for pebble flow

public:
  PebbleGame3D(int N, double box_size, unsigned int seed) : num_nodes(N) {
    std::mt19937 rng(seed); // deterministic seed for chunk reproducibility
    std::uniform_real_distribution<double> dist(0.0, box_size);

    lattice.reserve(N);
    pebbles.assign(N,
                   3); // 3 translation DOF pebbles per node for 3D (3,6) Game
    directed_edges.resize(N);

    for (int i = 0; i < N; ++i) {
      lattice.push_back({dist(rng), dist(rng), dist(rng)});
    }
  }

  // Breadth-First Search to find a free pebble and pull it to the target node
  bool pull_pebble(int target, int exclude1, int exclude2) {
    if (pebbles[target] > 0)
      return true;

    std::queue<int> q;
    std::vector<int> parent(num_nodes, -1);
    std::vector<bool> visited(num_nodes, false);

    q.push(target);
    visited[target] = true;
    visited[exclude1] = true;
    visited[exclude2] = true;

    int found_node = -1;

    while (!q.empty()) {
      int current = q.front();
      q.pop();

      if (pebbles[current] > 0) {
        found_node = current;
        break;
      }

      // Traverse incoming edges (which are physically directed edges OUT of
      // neighbors) Wait, standard pebble game: directed edge u->v means u
      // consumed a pebble to connect to v. We can reverse the edge to v->u,
      // returning a pebble to u and taking one from v. So we must search along
      // directed_edges.
      for (int neighbor : directed_edges[current]) {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          parent[neighbor] = current;
          q.push(neighbor);
        }
      }
    }

    if (found_node != -1) {
      // Reverse the path to flow the pebble to the target
      int curr = found_node;
      while (curr != target) {
        int p = parent[curr];
        // Reverse edge: curr -> p becomes p -> curr
        auto it = std::find(directed_edges[curr].begin(),
                            directed_edges[curr].end(), p);
        if (it != directed_edges[curr].end()) {
          directed_edges[curr].erase(it);
          directed_edges[p].push_back(curr);
        }
        curr = p;
      }
      pebbles[found_node]--;
      pebbles[target]++;
      return true;
    }
    return false;
  }

  // Attempts to add an independent bond between i and j
  bool add_bond(int i, int j) {
    // Collect up to 6 pebbles on i and j combined
    int internal_pebbles = pebbles[i] + pebbles[j];

    while (internal_pebbles < 6) {
      bool pushed = false;
      // Try pulling to i, protecting j
      if (pull_pebble(i, i, j)) {
        internal_pebbles++;
        pushed = true;
      } else if (pull_pebble(j, i, j)) {
        internal_pebbles++;
        pushed = true;
      }
      if (!pushed)
        break;
    }

    // If we gathered 6 pebbles, the bond is independent
    if (internal_pebbles == 6) {
      if (pebbles[i] > 0) {
        pebbles[i]--;
        directed_edges[i].push_back(j);
      } else {
        pebbles[j]--;
        directed_edges[j].push_back(i);
      }
      return true;
    }

    // Cannot gather 6 pebbles. Bond is redundant -> Rigidity Lock!
    return false;
  }

  double get_node_coord(int idx, int dim) {
    if (dim == 0)
      return lattice[idx].x;
    if (dim == 1)
      return lattice[idx].y;
    return lattice[idx].z;
  }
};

void process_boinc_workunit(int workunit_id, int N, double L, unsigned int seed,
                            const std::string &output_file) {
  boinc_begin_critical_section();
  // Simulate BOINC computation locally logging progress
  boinc_end_critical_section();

  PebbleGame3D engine(N, L, seed);

  double R_max = 2.5;
  int num_cells = std::max(1, (int)(L / R_max));
  double cell_size = L / num_cells;

  std::vector<std::vector<int>> grid(num_cells * num_cells * num_cells);

  for (int i = 0; i < N; ++i) {
    int cx =
        std::min((int)(engine.get_node_coord(i, 0) / cell_size), num_cells - 1);
    int cy =
        std::min((int)(engine.get_node_coord(i, 1) / cell_size), num_cells - 1);
    int cz =
        std::min((int)(engine.get_node_coord(i, 2) / cell_size), num_cells - 1);
    grid[cx + cy * num_cells + cz * num_cells * num_cells].push_back(i);
  }

  int total_independent = 0;
  int total_redundant = 0;

  double sweep_radii[] = {0.8, 1.2, 1.6, 2.0};
  double final_alpha_prediction = 0.0;

  for (double r : sweep_radii) {
    double r2 = r * r;
    int active_bonds = 0;
    int redundant = 0;

    for (int cx = 0; cx < num_cells; ++cx) {
      for (int cy = 0; cy < num_cells; ++cy) {
        for (int cz = 0; cz < num_cells; ++cz) {
          int grid_idx = cx + cy * num_cells + cz * num_cells * num_cells;
          auto &cell = grid[grid_idx];

          for (int i : cell) {
            for (int j : cell) {
              if (i >= j)
                continue;
              double dx =
                  engine.get_node_coord(i, 0) - engine.get_node_coord(j, 0);
              double dy =
                  engine.get_node_coord(i, 1) - engine.get_node_coord(j, 1);
              double dz =
                  engine.get_node_coord(i, 2) - engine.get_node_coord(j, 2);
              if (dx * dx + dy * dy + dz * dz <= r2) {
                if (engine.add_bond(i, j))
                  active_bonds++;
                else
                  redundant++;
              }
            }
          }
        }
      }
    }

    double p_c = (N * (4.0 / 3.0) * M_PI * std::pow(r / 2.0, 3)) / (L * L * L);
    double derived_inv_alpha = (8.0 * M_PI) / p_c;
    final_alpha_prediction = derived_inv_alpha;

    // Report incremental progress fraction roughly to BOINC Daemon
    boinc_fraction_done(r / 2.0);

    if (redundant > active_bonds * 0.1 && redundant > 100) {
      break;
    }
  }

  char resolved_path[256];
  boinc_resolve_filename(output_file.c_str(), resolved_path,
                         sizeof(resolved_path));
  std::ofstream out(resolved_path);
  out << "DERIVED_1_ALPHA=" << final_alpha_prediction << "\n";
  out.close();
}

int main(int argc, char **argv) {
  boinc_init();

  unsigned int seed = 42;
  int chunk_size = 500000;
  double bounding_box = 100.0;

  char input_path[256];
  boinc_resolve_filename("in.txt", input_path, sizeof(input_path));
  std::ifstream in(input_path);
  if (in.is_open()) {
    std::string line;
    while (std::getline(in, line)) {
      if (line.find("SEED=") == 0)
        seed = std::stoul(line.substr(5));
      if (line.find("CHUNK_SIZE=") == 0)
        chunk_size = std::stoi(line.substr(11));
      if (line.find("BOUNDING_BOX=") == 0)
        bounding_box = std::stod(line.substr(13));
    }
    in.close();
  } else {
    std::cerr << "Failed to open input file: " << input_path << std::endl;
  }

  process_boinc_workunit(seed, chunk_size, bounding_box, seed, "out.txt");

  boinc_finish(0);
  return 0;
}
