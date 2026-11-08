# Experiment plan (Week 1)

Owner: Nawrose Naomi

## Questions

1. Which route is best for a given objective: shortest distance or shortest time?
2. Which algorithm finds it with the least effort: BFS, UCS or A*?

## Measures recorded for every run

| Column | Meaning |
|---|---|
| algorithm | bfs, ucs, astar |
| objective | distance or time |
| start, goal | place names |
| cost | km or min |
| roads | number of roads in the path |
| expanded | nodes expanded |
| max_frontier | largest frontier size |
| time_ms | run time, averaged over repeated runs (`time.perf_counter`) |
| traffic | on / off |

## Experiments

| Experiment | What changes | Planned output |
|---|---|---|
| All pairs | Algorithm, objective (18 x 17 = 306 pairs) | Table of averages; bar chart of nodes expanded |
| Showcase | Start and goal (e.g. Bashundhara R/A to Dhanmondi 27, Uttara to Motijheel) | Map figures of the routes |
| Traffic | Jam on / off | Route before and after; change in cost |
| Objective | Distance vs time | Pairs where shortest is not fastest |

## Expected results (to be tested)

- UCS and A* always find the same cost (both optimal).
- A* expands fewer nodes (the heuristic guides it to the goal).
- BFS uses fewer roads but often costs more.
- For some pairs the shortest and fastest routes differ.

## Visualisation choice

networkx + matplotlib: places drawn at their real longitude/latitude; roads light grey; route thick red; start green square, goal blue triangle; a text box with the cost and nodes expanded. Charts use markers and line styles as well as colour, so they still read in black-and-white print.

## Week 2 plan

- `support/visualize.py`: draw the map and highlight a route
- Test with a hand-made route, then a UCS route; save example figures to `others/figures/`
