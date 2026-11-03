"""Набор простых тестов. Запуск: python -m unittest -v"""

import random
import unittest
from segment_tree import SegmentTree


class TestSegmentTree(unittest.TestCase):
    def setUp(self):
        self.tree = SegmentTree([5, 2, 8, 6, 1, 4, 7, 3])

    def test_sum_on_part_of_array(self):
        self.assertEqual(self.tree.query(1, 5, "sum"), 21)

    def test_minimum_and_maximum(self):
        self.assertEqual(self.tree.query(2, 6, "min"), 1)
        self.assertEqual(self.tree.query(2, 6, "max"), 8)

    def test_single_element(self):
        for operation in ("sum", "min", "max"):
            self.assertEqual(self.tree.query(3, 3, operation), 6)

    def test_update(self):
        changed = self.tree.update(3, 10)
        self.assertEqual(self.tree.query(1, 5, "sum"), 25)
        self.assertEqual(self.tree.query(0, 7, "max"), 10)
        self.assertIn(1, changed)

    def test_negative_values(self):
        tree = SegmentTree([-5, -2, -8])
        self.assertEqual(tree.query(0, 2, "sum"), -15)
        self.assertEqual(tree.query(0, 2, "min"), -8)
        self.assertEqual(tree.query(0, 2, "max"), -2)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            SegmentTree([])
        with self.assertRaises(IndexError):
            self.tree.query(5, 2)
        with self.assertRaises(IndexError):
            self.tree.update(100, 7)

    def test_against_simple_algorithm(self):
        rng = random.Random(17)
        values = [rng.randint(-50, 50) for _ in range(100)]
        tree = SegmentTree(values)
        for _ in range(100):
            a, b = sorted(rng.sample(range(len(values)), 2))
            self.assertEqual(tree.query(a, b, "sum"), sum(values[a:b+1]))
            self.assertEqual(tree.query(a, b, "min"), min(values[a:b+1]))
            self.assertEqual(tree.query(a, b, "max"), max(values[a:b+1]))
            index = rng.randrange(len(values))
            new_value = rng.randint(-100, 100)
            values[index] = new_value
            tree.update(index, new_value)


if __name__ == "__main__":
    unittest.main()
