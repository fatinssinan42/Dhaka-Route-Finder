"""Tests for BFS and UCS, using the hand-traced example from Week 1.

Toy map: Gulshan 1 (G), Mohakhali (M), Farmgate (F), Kawran Bazar (K),
Dhanmondi 27 (D) with draft distances in km.
"""

import unittest

from support.search import bfs, path_cost, ucs

# graph[place][neighbour] = (km, min)
TOY = {
    "G": {"M": (2.5, 14), "K": (5.5, 13)},
    "M": {"G": (2.5, 14), "F": (3.0, 12)},
    "F": {"M": (3.0, 12), "D": (2.2, 9)},
    "K": {"G": (5.5, 13), "D": (2.8, 11)},
    "D": {"F": (2.2, 9), "K": (2.8, 11)},
}


class UCSTest(unittest.TestCase):
    def test_matches_hand_trace(self):
        # Week 1 trace: expand G, M, K, F; the cheaper path to D (7.7) replaces 8.3
        path, cost, stats = ucs(TOY, "G", "D")
        self.assertEqual(path, ["G", "M", "F", "D"])
        self.assertAlmostEqual(cost, 7.7)
        self.assertEqual(stats["expanded"], 4)

    def test_time_objective(self):
        path, cost, _ = ucs(TOY, "G", "D", "time")
        self.assertEqual(path, ["G", "K", "D"])
        self.assertEqual(cost, 24)

    def test_start_is_goal(self):
        self.assertEqual(ucs(TOY, "M", "M")[:2], (["M"], 0))

    def test_unreachable(self):
        path, cost, _ = ucs({**TOY, "X": {}}, "G", "X")
        self.assertIsNone(path)
        self.assertEqual(cost, float("inf"))


class BFSTest(unittest.TestCase):
    def test_fewest_roads_but_not_cheapest(self):
        path, cost, stats = bfs(TOY, "G", "D")
        self.assertEqual(path, ["G", "K", "D"])
        self.assertAlmostEqual(cost, 8.3)
        self.assertEqual(stats["expanded"], 3)

    def test_start_is_goal(self):
        self.assertEqual(bfs(TOY, "D", "D")[:2], (["D"], 0))

    def test_unreachable(self):
        path, cost, _ = bfs({**TOY, "X": {}}, "G", "X")
        self.assertIsNone(path)
        self.assertEqual(cost, float("inf"))


class PathCostTest(unittest.TestCase):
    def test_path_cost(self):
        self.assertAlmostEqual(path_cost(TOY, ["G", "M", "F", "D"]), 7.7)
        self.assertEqual(path_cost(TOY, ["G", "M", "F", "D"], "time"), 35)


if __name__ == "__main__":
    unittest.main()
