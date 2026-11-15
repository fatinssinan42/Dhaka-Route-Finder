"""Uninformed search for the Dhaka Route Finder: BFS and UCS.

Graph format (shared with astar.py):
    graph[place][neighbour] = (distance_km, time_min)

Both functions return (path, cost, stats):
    path  - list of places from start to goal, or None if unreachable
    cost  - total distance (km) or time (min) of the path, by objective
    stats - nodes expanded, largest frontier size, run time in ms
"""

import heapq
import itertools
import math
import time
from collections import deque

COST_INDEX = {"distance": 0, "time": 1}


def path_cost(graph, path, objective="distance"):
    """Total cost of a path under the chosen objective."""
    idx = COST_INDEX[objective]
    return sum(graph[a][b][idx] for a, b in zip(path, path[1:]))


def bfs(graph, start, goal, objective="distance"):
    """Breadth-first search: finds the route with the fewest roads.

    Ignores road costs, so the route is only optimal when every road costs
    the same. The goal is tested when a place is generated. The objective
    is used only to report the cost of the route found.
    """
    t0 = time.perf_counter()
    if start == goal:
        return [start], 0, _stats(0, 1, t0)
    frontier = deque([start])
    parent = {start: None}
    expanded = 0
    max_frontier = 1

    while frontier:
        node = frontier.popleft()
        expanded += 1
        for nbr in graph[node]:
            if nbr in parent:
                continue
            parent[nbr] = node
            if nbr == goal:
                path = _rebuild(parent, goal)
                return path, path_cost(graph, path, objective), _stats(expanded, max_frontier, t0)
            frontier.append(nbr)
        max_frontier = max(max_frontier, len(frontier))

    return None, math.inf, _stats(expanded, max_frontier, t0)


def ucs(graph, start, goal, objective="distance"):
    """Uniform cost search: always expands the cheapest path g(n) first.

    Optimal for non-negative costs. The goal is tested when a place is
    removed from the queue, not when it is added; otherwise a more
    expensive path found first could be returned.
    """
    idx = COST_INDEX[objective]
    t0 = time.perf_counter()
    tie = itertools.count()  # equal costs leave the queue in insertion order
    frontier = [(0, next(tie), start)]
    best = {start: 0}
    parent = {start: None}
    expanded = 0
    max_frontier = 1

    while frontier:
        g, _, node = heapq.heappop(frontier)
        if g > best[node]:
            continue  # outdated entry, a cheaper path was found later
        if node == goal:
            return _rebuild(parent, goal), g, _stats(expanded, max_frontier, t0)
        expanded += 1
        for nbr, costs in graph[node].items():
            new_g = g + costs[idx]
            if new_g < best.get(nbr, math.inf):
                best[nbr] = new_g
                parent[nbr] = node
                heapq.heappush(frontier, (new_g, next(tie), nbr))
        max_frontier = max(max_frontier, len(frontier))

    return None, math.inf, _stats(expanded, max_frontier, t0)


def _rebuild(parent, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


def _stats(expanded, max_frontier, t0):
    return {
        "expanded": expanded,
        "max_frontier": max_frontier,
        "time_ms": (time.perf_counter() - t0) * 1000,
    }
