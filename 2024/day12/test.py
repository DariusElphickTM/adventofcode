import unittest
from farm_fencing_calculator import FarmFencingCalculator

class TestFarmFencingCalculator(unittest.TestCase):
    
    simple_example_input = """AAAA
BBCD
BBCC
EEEC"""

    larger_example_input = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

    complex_example_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

    e_example_input = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""

    abba_example_input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

    def setUp(self):
        self.default_test_calculator = FarmFencingCalculator(self.complex_example_input)
    
    def test_creates_adjacency_matrix_for_simple_example(self):
        test_calculator = FarmFencingCalculator(self.simple_example_input)
        self.assertListEqual(["A","A","A","A","B","B","C","D","B","B","C","C","E","E","E","C"], test_calculator.plots)
        self.assertListEqual([
            [
                0, 1, 0, 0, 
                2, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                1, 0, 1, 0, 
                0, 2, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, 1, 0, 1, 
                0, 0, 2, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, 0, 1, 0, 
                0, 0, 0, 2, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                2, 0, 0, 0, 
                0, 1, 0, 0, 
                1, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, 2, 0, 0, 
                1, 0, 2, 0, 
                0, 1, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, 0, 2, 0, 
                0, 2, 0, 2, 
                0, 0, 1, 0, 
                0, 0, 0, 0
            ],
            [
                0, 0, 0, 2, 
                0, 0, 2, 0, 
                0, 0, 0, 2, 
                0, 0, 0, 0
            ],
            [
                0, 0, 0, 0, 
                1, 0, 0, 0, 
                0, 1, 0, 0, 
                2, 0, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, 1, 0, 0, 
                1, 0, 2, 0, 
                0, 2, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 1, 0, 
                0, 2, 0, 1, 
                0, 0, 2, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 2, 
                0, 0, 1, 0, 
                0, 0, 0, 1
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                2, 0, 0, 0, 
                0, 1, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 2, 0, 0, 
                1, 0, 1, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 2, 0, 
                0, 1, 0, 2
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 1, 
                0, 0, 2, 0
            ]
        ], test_calculator.plot_adjacency_matrix)
    
    """def test_returns_correct_cost_for_simple_example(self):
        test_calculator = FarmFencingCalculator(self.simple_example_input)
        self.assertEqual(test_calculator.get_total_cost(), 140)
    
    def test_returns_correct_discounted_cost_for_simple_example(self):
        test_calculator = FarmFencingCalculator(self.simple_example_input)
        self.assertEqual(test_calculator.get_total_discounted_cost(), 80)""" 
    
    def test_finds_correct_regions_for_simple_example(self):
        test_calculator = FarmFencingCalculator(self.simple_example_input)
        self.assertListEqual([
            {
                'plant': 'A',
                'area': 4,
                'perimeter': 10,
                'sides': 4
            },
            {
                'plant': 'B',
                'area': 4,
                'perimeter': 8,
                'sides': 4
            },
            {
                'plant': 'C',
                'area': 4,
                'perimeter': 10,
                'sides': 8
            },
            {
                'plant': 'D',
                'area': 1,
                'perimeter': 4,
                'sides': 4
            },
            {
                'plant': 'E',
                'area': 3,
                'perimeter': 8,
                'sides': 4
            }
        ], test_calculator.find_regions())
    
    """def test_returns_correct_cost_for_larger_example(self):
        test_calculator = FarmFencingCalculator(self.larger_example_input)
        self.assertEqual(test_calculator.get_total_cost(), 772)
    
    def test_returns_correct_discounted_cost_for_larger_example(self):
        test_calculator = FarmFencingCalculator(self.larger_example_input)
        self.assertEqual(test_calculator.get_total_discounted_cost(), 436)
    
    def test_returns_correct_cost_for_complex_example(self):
        test_calculator = FarmFencingCalculator(self.complex_example_input)
        self.assertEqual(test_calculator.get_total_cost(), 1930)
    
    def test_returns_correct_discounted_cost_for_complex_example(self):
        test_calculator = FarmFencingCalculator(self.complex_example_input)
        self.assertEqual(test_calculator.get_total_discounted_cost(), 1206)
    
    def test_returns_correct_discounted_cost_for_e_example(self):
        test_calculator = FarmFencingCalculator(self.e_example_input)
        self.assertEqual(test_calculator.get_total_discounted_cost(), 236)
    
    def test_returns_correct_discounted_cost_for_abba_example(self):
        test_calculator = FarmFencingCalculator(self.abba_example_input)
        self.assertEqual(test_calculator.get_total_discounted_cost(), 368)"""

if __name__ == "__main__":
    unittest.main()