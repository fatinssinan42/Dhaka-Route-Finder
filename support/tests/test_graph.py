"""Tests for the map data and the graph loader."""

import tempfile
import unittest
from pathlib import Path

from support.graph import load_map, validate


class RealMapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph, cls.coords = load_map()

    def test_size(self):
        self.assertEqual(len(self.coords), 18)
        self.assertEqual(sum(len(n) for n in self.graph.values()) // 2, 30)

    def test_roads_are_two_way(self):
        for a, nbrs in self.graph.items():
            for b, costs in nbrs.items():
                self.assertEqual(self.graph[b][a], costs)

    def test_map_has_no_problems(self):
        self.assertEqual(validate(self.graph, self.coords), [])


class ValidateTest(unittest.TestCase):
    def _load(self, places, roads):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "places.csv").write_text("name,lat,lon\n" + places)
            Path(d, "roads.csv").write_text("from,to,distance_km,time_min\n" + roads)
            return load_map(d)

    def test_road_shorter_than_straight_line(self):
        graph, coords = self._load("A,23.78,90.40\nB,23.75,90.39\n", "A,B,1.0,5\n")
        self.assertIn("shorter than the straight line", validate(graph, coords)[0])

    def test_unreachable_place(self):
        graph, coords = self._load(
            "A,23.78,90.40\nB,23.75,90.39\nC,23.70,90.30\nD,23.71,90.31\n",
            "A,B,5.0,15\nC,D,3.0,10\n",
        )
        self.assertTrue(any("cannot be reached" in p for p in validate(graph, coords)))

    def test_unknown_place_name(self):
        with self.assertRaises(ValueError):
            self._load("A,23.78,90.40\n", "A,Dhanmondi,2.0,5\n")


if __name__ == "__main__":
    unittest.main()
