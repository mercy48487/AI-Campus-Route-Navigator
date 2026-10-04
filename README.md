# AI Campus Route Navigator — Assignment X_03

Python implementation of two campus route-search agents:
- **PATHFINDER:** Greedy Best-First Search, priority `h(n)`
- **ORBIT:** A* Search, priority `g(n) + h(n)`

## Files
- `main.py` — command-line interface
- `campus_map.py` — loads the weighted graph and calculates the heuristic
- `search.py` — search algorithms and CSE-zone transition restriction
- `agents.py` — PATHFINDER and ORBIT classes
- `experiment.py` — runs five source/destination pairs and writes `results.csv`
- `campus.json` — graph data kept separate from the algorithms
- `results.csv` — generated experiment results
- `BRIEF_REPORT.md` — concise report

## Run (Python 3.9+)
No external packages are required.

```bash
python main.py
```

Enter start and destination using the exact spelling shown in the location list. The program prints both agents' route, path cost, explored nodes and runtime. It also runs the five comparison experiments and refreshes `results.csv`.

## Important graph note
The node names are taken from the supplied satellite map. The connections, coordinate estimates and metre weights in `campus.json` are an initial illustrative model inferred from the map, not surveyed measurements. Confirm them against walkable campus paths and update `campus.json` if needed before final submission.

## Algorithms
Greedy Best-First selects the frontier node with the smallest heuristic value. A* selects the node with the smallest sum of path-so-far cost and heuristic estimate. Neither algorithm uses a pre-built pathfinding library.

The CSE-zone rule is enforced while generating successors: CSE locations are reached through a Tower 2 entry and Lift Area; once inside, movement is limited to CSE locations until returning to the Lift Area, then exiting via a Tower 2 entry.
