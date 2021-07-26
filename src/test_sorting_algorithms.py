import unittest

from sorting_algorithms import *


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self) -> None:
        input_size = 1000
        self.best_case_input = list(range(1, input_size + 1))
        self.worst_case_input = list(range(input_size, 0, -1))

    def test_insertion_sort(self):
        expected_result = self.best_case_input
        result = insertion_sort(self.worst_case_input)

        self.assertListEqual(result, expected_result)

    def test_selection_sort(self):
        expected_result = self.best_case_input
        result = selection_sort(self.worst_case_input)

        self.assertListEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
