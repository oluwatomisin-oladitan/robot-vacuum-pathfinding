# Robot Vacuum Cleaner Pathfinding Algorithm

## Overview
A Python implementation of a pathfinding algorithm for a robot vacuum cleaner navigating a grid-based map. The robot must clean all stained cells while avoiding obstacles, using Breadth-First Search (BFS) to find the optimal path.

## How It Works
1. Reads a grid map from a CSV file
2. Locates the robot's starting position and all stains
3. Calculates Euclidean distances from robot to each stain
4. Solves the map using BFS, visiting nearest stains first

## Map Notation
| Symbol | Meaning |
|--------|---------|
| . | Clean floor |
| @ | Stain |
| # | Robot starting position |
| x | Obstacle |

## Functions
- **readMap()** — reads CSV map file into 2D list
- **locate()** — finds robot start and stain coordinates
- **calculateDistances()** — calculates Euclidean distances to each stain
- **solveMap()** — solves map using BFS, returns path string (U/D/L/R)

## Technologies
- Python
- BFS algorithm
- Math module
