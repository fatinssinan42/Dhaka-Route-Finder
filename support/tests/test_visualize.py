"""Tests for the map drawing, using a small hand-made map and route."""

import tempfile
import unittest
from pathlib import Path

from matplotlib.collections import PathCollection

from support.visualize import draw_map

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


if __name__ == "__main__":
    unittest.main()
