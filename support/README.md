# support

Code used by `main.py`.

| Module | Purpose |
|---|---|
| `graph.py` | Load `data/` into a graph: `graph[place][neighbour] = (km, min)` |
| `search.py` | BFS and UCS |
| `astar.py` | A* search and heuristics |
| `visualize.py` | Draw the map and highlight a route |
| `experiments.py` | Run the algorithm comparisons and save results |

Every search function returns `(path, cost, stats)`, where `stats` holds the
number of nodes expanded, the largest frontier size and the run time.
