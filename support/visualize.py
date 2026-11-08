"""Draw the Dhaka map and highlight a route.

Each place is drawn at its real longitude (x) and latitude (y), so the
picture keeps the shape of the city. All roads are light grey; the route
is thick and coloured, the start is green and the goal is blue.

Run this file to save an example figure of a UCS route to others/figures/.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # draw to files; no window needed
import matplotlib.pyplot as plt  # noqa: E402
import networkx as nx  # noqa: E402

ROUTE_COLOUR = "#d62728"
START_COLOUR = "#2ca02c"
GOAL_COLOUR = "#1f77b4"
# Where to put a place's name in crowded parts of the map (default: above)
LABEL_SIDE = {"Badda": "right", "Dhanmondi 27": "left", "Kawran Bazar": "below", "Farmgate": "right",
              "Mohammadpur": "left", "Malibagh": "right", "Shahbag": "right", "New Market": "below", "Motijheel": "below"}


def draw_map(graph, coords, path=None, title=None, info=None, ax=None, save_path=None):
    """Draw graph[place][neighbour] = (km, min) with an optional highlighted path.

    info is a short text (for example cost and nodes expanded) shown in a box.
    Returns the matplotlib Axes. If save_path is given the figure is saved.
    """
    g = nx.Graph()
    for a, nbrs in graph.items():
        g.add_node(a)
        for b in nbrs:
            g.add_edge(a, b)
    pos = {p: (lon, lat) for p, (lat, lon) in coords.items()}

    own_fig = ax is None
    if own_fig:
        _, ax = plt.subplots(figsize=(8, 8))

    nx.draw_networkx_edges(g, pos, ax=ax, edge_color="#c8c8c8", width=1.5)
    nx.draw_networkx_nodes(g, pos, ax=ax, node_color="#ffffff", edgecolors="#555555", node_size=120)

    if path:
        route = list(zip(path, path[1:]))
        nx.draw_networkx_edges(g, pos, edgelist=route, ax=ax, edge_color=ROUTE_COLOUR, width=4)
        nx.draw_networkx_nodes(g, pos, nodelist=path[1:-1], ax=ax, node_color=ROUTE_COLOUR, node_size=120)
        nx.draw_networkx_nodes(g, pos, nodelist=[path[0]], ax=ax, node_color=START_COLOUR,
                               node_shape="s", node_size=220)
        nx.draw_networkx_nodes(g, pos, nodelist=[path[-1]], ax=ax, node_color=GOAL_COLOUR,
                               node_shape="^", node_size=260)

    for place, (x, y) in pos.items():
        side = LABEL_SIDE.get(place, "above")
        dx, dy, ha, va = {"above": (0, 0.003, "center", "bottom"), "below": (0, -0.003, "center", "top"),
                          "left": (-0.003, 0, "right", "center"), "right": (0.003, 0, "left", "center")}[side]
        ax.text(x + dx, y + dy, place, fontsize=8, ha=ha, va=va)
    ax.margins(0.12)

    if info:
        ax.text(0.02, 0.02, info, transform=ax.transAxes, fontsize=9, va="bottom",
                bbox=dict(boxstyle="round", facecolor="white", edgecolor="#999999"))
    ax.set_title(title or "Dhaka Route Finder")
    ax.set_xlabel("Longitude (°E)")
    ax.set_ylabel("Latitude (°N)")
    ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    ax.set_aspect("equal")

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        ax.figure.savefig(save_path, dpi=150, bbox_inches="tight")
    if own_fig and save_path:
        plt.close(ax.figure)
    return ax


if __name__ == "__main__":
    from support.graph import load_map
    from support.search import ucs

    graph, coords = load_map()
    start, goal = "Gulshan 1", "Dhanmondi 27"
    out = Path(__file__).resolve().parent.parent / "others" / "figures"

    for objective, unit in (("distance", "km"), ("time", "min")):
        path, cost, stats = ucs(graph, start, goal, objective)
        info = f"UCS, {objective}: {cost:g} {unit}\nnodes expanded: {stats['expanded']}"
        file = out / f"week2_ucs_{objective}.png"
        draw_map(graph, coords, path, f"{start} to {goal} ({'shortest' if objective == 'distance' else 'fastest'})",
                 info, save_path=file)
        print(f"{objective}: {' -> '.join(path)} = {cost:g} {unit}; saved {file.name}")
