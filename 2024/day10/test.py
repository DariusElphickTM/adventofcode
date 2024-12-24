import unittest
from trail_finder import TrailFinder

class TestTrailFinder(unittest.TestCase):
    example_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    simple_example = """0123
1234
8765
9876"""
    
    def setUp(self):
        self.default_trail_finder = TrailFinder(16)
        self.default_trail_finder.parse_input(self.simple_example)
    
    def test_should_return_correct_result_for_example(self):
        test_trail_finder = TrailFinder()
        test_trail_finder.parse_input(self.example_input)
        self.assertEqual(test_trail_finder.get_score_for_all_trailheads(), 36)
    
    def test_should_return_correct_result_for_simple_example_with_one_trail(self):
        self.assertEqual(self.default_trail_finder.get_trailhead_score(0), 16)
    
    def test_should_parse_input_string_and_produce_adjacency_matrix_for_simple_data_set(self):
        expected_trail_postions = ['0', '1', '2', '3', '1', '2', '3', '4', '8', '7', '6', '5', '9', '8', '7', '6']
        expected_trail_map = [
            [
                0, 1, 0, 0, 
                1, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                -1, 0, 1, 0, 
                0, 1, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, -1, 0, 1, 
                0, 0, 1, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, 0, -1, 0, 
                0, 0, 0, 1, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                -1, 0, 0, 0, 
                0, 1, 0, 0, 
                7, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, -1, 0, 0, 
                -1, 0, 1, 0, 
                0, 5, 0, 0,
                0, 0, 0, 0
            ],
            [
                0, 0, -1, 0, 
                0, -1, 0, 1, 
                0, 0, 3, 0, 
                0, 0, 0, 0
            ],
            [
                0, 0, 0, -1, 
                0, 0, -1, 0, 
                0, 0, 0, 1, 
                0, 0, 0, 0
            ],
            [
                0, 0, 0, 0, 
                -7, 0, 0, 0, 
                0, -1, 0, 0, 
                1, 0, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, -5, 0, 0,
                1, 0, -1, 0, 
                0, 1, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, -3, 0, 
                0, 1, 0, -1, 
                0, 0, 1, 0
            ],
            [
                0, 0, 0, 0,
                0, 0, 0, -1, 
                0, 0, 1, 0, 
                0, 0, 0, 1
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                -1, 0, 0, 0, 
                0, -1, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, -1, 0, 0, 
                1, 0, -1, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, -1, 0, 
                0, 1, 0, -1
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, -1, 
                0, 0, 1, 0
            ]
        ]
        self.assertListEqual(self.default_trail_finder.trail_positions, expected_trail_postions)
        self.assertListEqual(self.default_trail_finder.trail_map, expected_trail_map)
    
    def test_should_add_and_recover_edges(self):
        test_trail_finder = TrailFinder(3)
        test_trail_finder.add_edge(0, 1, 1)
        test_trail_finder.add_edge(1, 2, 1)
        test_trail_finder.add_edge(2, 1, 2)
        
        self.assertEqual(test_trail_finder.get_edge(0, 1), 1)
        self.assertEqual(test_trail_finder.get_edge(1, 2), 1)
        self.assertEqual(test_trail_finder.get_edge(2, 1), 2)
        self.assertEqual(test_trail_finder.get_edge(1, 0), 0)
        self.assertEqual(test_trail_finder.get_edge(0, 2), 0)
        self.assertEqual(test_trail_finder.get_edge(2, 0), 0)
    
    def test_should_get_trailhead_indexes_for_simple_example(self):
        self.assertListEqual([0], self.default_trail_finder.get_trailhead_indexes())
    
    def test_should_get_trailhead_indexes_for_example(self):
        test_trail_finder = TrailFinder()
        test_trail_finder.parse_input(self.example_input)
        self.assertListEqual([2, 4, 20, 38, 42, 45, 48, 54, 57], test_trail_finder.get_trailhead_indexes())

if __name__ == "__main__":
    unittest.main()