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

Present: Abdullah, Pakeezah, Fatin, Nawrose

**Done**
- Map data: 18 places and 30 roads with km and minutes; loader checks pass.
- BFS and UCS match the Week 1 hand trace; A* gives the same costs as UCS with fewer expansions.
- Map drawing with the route highlighted; first two figures (shortest vs fastest).

**Next (Week 3)**
| Who | Task |
|---|---|
| Abdullah | Road names and types (highway, main, busy) in the data |
| Pakeezah | Step-by-step directions for a route |
| Fatin | `main.py` text menu and command-line options |
| Nawrose | Side-by-side BFS / UCS / A* figure |

## Week 3 (Nov 15 – Nov 21)

Present: Abdullah, Pakeezah, Fatin, Nawrose

**Done**
- Road names and types added; directions merge steps on the same road.
- `main.py` runs all three algorithms and prints a comparison table.
- Comparison figure: BFS uses fewer roads but a longer route than UCS and A*.

**Next (Week 4: project update in class 12)**
| Who | Task |
|---|---|
| Everyone | Own 2-page update report; own part of the 5-minute talk |
| Nawrose | Update slides |
| Fatin | README refresh, final repo check before the deadline |
