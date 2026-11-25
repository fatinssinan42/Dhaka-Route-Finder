"""Tests for the map drawing, using a small hand-made map and route."""

import tempfile
import unittest
from pathlib import Path

from matplotlib.collections import PathCollection

from support.visualize import compare_figure, draw_map

TOY = {
    "Gulshan 1": {"Mohakhali": (2.4, 14)},
    "Mohakhali": {"Gulshan 1": (2.4, 14), "Farmgate": (3.2, 13)},
    "Farmgate": {"Mohakhali": (3.2, 13)},
}
COORDS = {
    "Gulshan 1": (23.781, 90.417),
    "Mohakhali": (23.778, 90.400),
    "Farmgate": (23.758, 90.390),
}


class DrawMapTest(unittest.TestCase):
    def test_saves_figure_with_route(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "route.png"
            draw_map(TOY, COORDS, ["Gulshan 1", "Mohakhali", "Farmgate"], "Test", "cost: 5.6 km", save_path=out)
            self.assertTrue(out.exists())
            self.assertGreater(out.stat().st_size, 1000)

    def test_draws_without_route(self):
        ax = draw_map(TOY, COORDS)
        self.assertEqual(ax.get_title(), "Dhaka Route Finder")
        # places are placed at (longitude, latitude)
        xs = [x for coll in ax.collections if isinstance(coll, PathCollection) for x, _ in coll.get_offsets()]
        self.assertAlmostEqual(min(xs), 90.390)

    def test_explored_places_are_shaded(self):
        ax = draw_map(TOY, COORDS, explored=["Gulshan 1", "Mohakhali"])
        # one node layer for all places, one for the explored places
        layers = [c for c in ax.collections if isinstance(c, PathCollection)]
        self.assertEqual(len(layers), 2)
        self.assertEqual(len(layers[1].get_offsets()), 2)


class CompareFigureTest(unittest.TestCase):
    def test_one_panel_per_algorithm(self):
        path = ["Gulshan 1", "Mohakhali", "Farmgate"]
        stats = {"expanded": 2, "max_frontier": 1, "time_ms": 0.1}
        results = [{"label": name, "path": path, "cost": 5.6, "unit": "km", "stats": stats} for name in ("BFS", "UCS", "A*")]
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "compare.png"
            fig = compare_figure(TOY, COORDS, results, "Test", out)
            self.assertTrue(out.exists())
        self.assertEqual([ax.get_title() for ax in fig.axes], ["BFS", "UCS", "A*"])


if __name__ == "__main__":
    unittest.main()
