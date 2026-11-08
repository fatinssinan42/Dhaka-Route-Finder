# Meeting notes

Kept by Nawrose Naomi. Three lines per meeting: what was done, what is next, who owns it.

## Week 1 (Nov 1 – Nov 7)

Present: Abdullah, Pakeezah, Fatin, Nawrose

**Decided**
- Project: Dhaka Route Finder (BFS, UCS, A* on a map of Dhaka; shortest vs fastest route).
- Roles: Abdullah map data; Pakeezah problem formulation, BFS and UCS; Fatin GitHub, A* and heuristics; Nawrose visualisation, experiments and documents.
- Shared graph format: `graph[place][neighbour] = (km, min)`. Every search returns `(path, cost, stats)`.
- Each member commits their own work, at least twice a week.

**Next (Week 2)**
| Who | Task |
|---|---|
| Abdullah | `data/roads.csv`, `support/graph.py` loader with checks, tests |
| Pakeezah | `support/search.py` (BFS, UCS), tests matching the hand trace |
| Fatin | `support/astar.py` (A*, heuristics), admissibility check, tests |
| Nawrose | `support/visualize.py` (map drawing), tests, example figures |

## Week 2 (Nov 8 – Nov 14)

Present:

**Done**
-

**Next (Week 3)**
-
