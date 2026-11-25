"""Load the Dhaka map from data/ and check it for errors.

    places.csv: name, lat, lon
    roads.csv:  from, to, distance_km, time_min   (roads are two-way)

The map is returned as:
    graph[place][neighbour] = (distance_km, time_min)
    coords[place] = (lat, lon)
"""

import csv
from collections import deque
from pathlib import Path

from support.geo import haversine_km

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_places(path=DATA_DIR / "places.csv"):
    with open(path, newline="", encoding="utf-8") as f:
        return {row["name"].strip(): (float(row["lat"]), float(row["lon"])) for row in csv.DictReader(f)}


def load_roads(places, path=DATA_DIR / "roads.csv"):
    graph = {name: {} for name in places}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            a, b = row["from"].strip(), row["to"].strip()
            costs = (float(row["distance_km"]), float(row["time_min"]))
            for x, y in ((a, b), (b, a)):
                if x not in graph:
                    raise ValueError(f"Unknown place in roads.csv: {x!r}")
                graph[x][y] = costs
    return graph


def load_map(data_dir=DATA_DIR):
    """Return (graph, coords) for the whole map."""
    coords = load_places(Path(data_dir) / "places.csv")
    graph = load_roads(coords, Path(data_dir) / "roads.csv")
    return graph, coords


def validate(graph, coords):
    """Return a list of problems found in the map (empty if the map is fine)."""
    problems = []
    for a, nbrs in graph.items():
        for b, (km, mins) in nbrs.items():
            if a >= b:
                continue  # check each two-way road once
            if km <= 0 or mins <= 0:
                problems.append(f"{a} - {b}: costs must be positive")
            straight = haversine_km(coords[a], coords[b])
            if km < straight:
                problems.append(f"{a} - {b}: {km} km is shorter than the straight line ({straight:.2f} km)")

    isolated = [p for p, nbrs in graph.items() if not nbrs]
    problems += [f"{p}: no roads" for p in isolated]

    start = next(iter(graph))
    seen = {start}
    queue = deque([start])
    while queue:
        for nbr in graph[queue.popleft()]:
            if nbr not in seen:
                seen.add(nbr)
                queue.append(nbr)
    problems += [f"{p}: cannot be reached from {start}" for p in graph if p not in seen and p not in isolated]
    return problems


if __name__ == "__main__":
    g, c = load_map()
    roads = sum(len(n) for n in g.values()) // 2
    print(f"{len(g)} places, {roads} roads")
    issues = validate(g, c)
    print("\n".join(issues) if issues else "Map OK: no problems found")
