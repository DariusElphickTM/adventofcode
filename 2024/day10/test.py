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
        self.default_trail_finder = TrailFinder(self.simple_example)
    
    def test_should_return_correct_result_for_example(self):
        test_trail_finder = TrailFinder(self.example_input)
        self.assertEqual(test_trail_finder.get_trailhead_score(), 36)
    
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
                0, 0, -1, 0, 
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

if __name__ == "__main__":
    unittest.main()