# A* design (Week 1)

Owner: Fatin Sadab Sinan

## Idea

A* expands the node with the smallest

    f(n) = g(n) + h(n)

where g(n) is the cost so far and h(n) estimates the cost still needed. In the course notes this is UCS run on modified edge costs:

    C(s1 -> s2) = C0(s1 -> s2) + h(s2) - h(s1)

A* returns an optimal route when h never overestimates the true remaining cost (h is **admissible**).

## Heuristic for each objective

| Objective | h(n) | Why it is admissible |
|---|---|---|
| Distance (km) | Straight-line (haversine) distance from n to the goal | No road is shorter than the straight line between its ends |
| Time (min) | Straight-line distance / v_max x 60 | v_max is the highest speed on any road, so no real route can be faster |

Haversine distance between (lat1, lon1) and (lat2, lon2), R = 6371 km:

    d = 2R asin( sqrt( sin^2(dlat/2) + cos(lat1) cos(lat2) sin^2(dlon/2) ) )

`v_max` is computed from the map itself (the largest km / hour over all roads), so the time heuristic stays admissible even when the road data changes.

Example: Gulshan 1 to Dhanmondi 27 is about 5.1 km in a straight line, while the shortest road route is 7.7 km, so h underestimates as required.

## Pseudocode

```
frontier = priority queue ordered by f = g + h
push (h(start), start), g(start) = 0
while frontier not empty:
    pop node with smallest f
    if g(node) is out of date: skip
    if node == goal: return path, g(node), stats
    expanded += 1
    for each neighbour:
        new_g = g(node) + cost(node, neighbour)
        if new_g < best g(neighbour):
            store new_g, parent, push (new_g + h(neighbour), neighbour)
return no path
```

Ties are broken by insertion order (a counter in each queue entry), the same as in UCS, so results are repeatable.

## Shared output format

Agreed with Pakeezah (BFS, UCS) and Nawrose (experiments): every search returns `(path, cost, stats)` with `stats = {expanded, max_frontier, time_ms}`.

## Week 2 plan

- `support/astar.py`: A* with both heuristics
- Tests on the 5-place toy map, plus a check that h(n) <= true cost for every place
