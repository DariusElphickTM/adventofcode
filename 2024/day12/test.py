import unittest
from farm_fencing_calculator import FarmFencingCalculator

class TestFarmFencingCalculator(unittest.TestCase):
    
    simple_example_input = """AAAA
BBCD
BBCC
EEEC"""

    larger_example_input = """RRRRIICCFF
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
        self.default_test_calculator = FarmFencingCalculator(self.larger_example_input)
    
    def test_parses_simple_example_correctly(self):
        test_calculator = FarmFencingCalculator(self.simple_example_input)
        self.assertListEqual([
            ["A","A","A","A"],
            ["B","B","C","D"],
            ["B","B","C","C"],
            ["E","E","E","C"]
        ], test_calculator.farm_map)

if __name__ == "__main__":
    unittest.main()