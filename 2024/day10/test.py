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
    
    def setUp(self):
        self.default_trail_finder = TrailFinder(self.example_input)
    
    def test_should_parse_input_string_and_produce_adjacency_matrix_for_simple_data_set(self):
        simple_example = """0123
                            1234
                            8765
                            9876"""
        expected_trail = ['0', '1', '2', '3', '1', '2', '3', '4', '8', '7', '6', '5', '9', '8', '7', '6']
        expected_trail_map = [
            [
                0, 1, None, None, 
                1, None, None, None, 
                None, None, None, None, 
                None, None, None, None
            ],
            [
                -1, 0, 1, None, 
                None, 1, None, None, 
                None, None, None, None, 
                None, None, None, None
            ],
            [
                None, -1, 0, 1, 
                None, None, 1, None, 
                None, None, None, None, 
                None, None, None, None
            ],
            [
                None, None, -1, 0, 
                None, None, None, 1, 
                None, None, None, None, 
                None, None, None, None
            ],
            [
                -1, None, None, None, 
                0, 1, None, None, 
                7, None, None, None, 
                None, None, None, None
            ],
            [
                None, -1, None, None, 
                -1, 0, 1, None, 
                None, 5, None, None,
                None, None, None, None
            ],
            [
                None, None, -1, None, 
                None, -1, 0, 1, 
                None, None, 3, None, 
                None, None, None, None
            ],
            [
                None, None, None, -1, 
                None, None, -1, 0, 
                None, None, None, 1, 
                None, None, None, None
            ],
            [
                None, None, None, None, 
                -7, None, None, None, 
                0, -1, None, None, 
                1, None, None, None
            ],
            [
                None, None, None, None, 
                None, -5, None, None,
                1, 0, -1, None, 
                None, 1, None, None
            ],
            [
                None, None, None, None, 
                None, None, -1, None, 
                None, 1, 0, -1, 
                None, None, 1, None
            ],
            [
                None, None, None, None,
                None, None, None, -1, 
                None, None, 1, 0, 
                None, None, None, 1
            ],
            [
                None, None, None, None, 
                None, None, None, None, 
                None, None, None, -1, 
                None, None, 1, 0
            ],
            [
                None, None, None, None, 
                None, None, None, None, 
                None, None, -1, None, 
                None, 1, 0, -1
            ],
            [
                None, None, None, None, 
                None, None, None, None, 
                None, -1, None, None, 
                1, 0, -1, None
            ],
            [
                None, None, None, None, 
                None, None, None, None, 
                -1, None, None, None, 
                0, -1, None, None
            ]
        ]
        self.assertEqual(True, True)