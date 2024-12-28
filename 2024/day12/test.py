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

    def setUp(self):
        self.default_test_calculator = FarmFencingCalculator(self.complex_example_input)
    
    def test_parses_simple_example_correctly(self):
        test_calculator = FarmFencingCalculator(self.simple_example_input)
        self.assertListEqual([
            ["A","A","A","A"],
            ["B","B","C","D"],
            ["B","B","C","C"],
            ["E","E","E","C"]
        ], test_calculator.farm_map)
    
    def test_returns_correct_cost_for_simple_example(self):
        test_calculator = FarmFencingCalculator(self.simple_example_input)
        self.assertEqual(test_calculator.get_total_cost(), 140)
    
    def test_returns_correct_cost_for_larger_example(self):
        test_calculator = FarmFencingCalculator(self.larger_example_input)
        self.assertEqual(test_calculator.get_total_cost(), 772)
    
    def test_returns_correct_cost_for_complex_example(self):
        test_calculator = FarmFencingCalculator(self.complex_example_input)
        self.assertEqual(test_calculator.get_total_cost(), 1930)

if __name__ == "__main__":
    unittest.main()