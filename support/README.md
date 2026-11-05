# support

Code used by `main.py`.

| Module | Owner | Purpose |
|---|---|---|
| `geo.py` | Fatin | Straight-line (haversine) distance between two places |
| `graph.py` | Abdullah | Load `data/` into a graph: `graph[place][neighbour] = (km, min)`, and check it |
| `search.py` | Pakeezah | BFS and UCS |
| `astar.py` | Fatin | A* search and heuristics |
| `visualize.py` | Nawrose | Draw the map and highlight a route |
| `experiments.py` | Nawrose | Run the algorithm comparisons and save results |
| `tests/` | everyone | One test file per module |

Every search function returns `(path, cost, stats)`, where `stats` holds the
number of nodes expanded, the largest frontier size and the run time.
