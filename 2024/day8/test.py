import unittest
import huge_antenna

class TestHugeAntenna(unittest.TestCase):
    
    test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    
    def setUp(self):
        self.default_test_antenna = huge_antenna.HugeAntenna(self.test_input)
    
    def test_it_parses_input_correctly(self):
        self.assertListEqual([
            ['.','.','.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','0','.','.','.'],
            ['.','.','.','.','.','0','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','0','.','.','.','.'],
            ['.','.','.','.','0','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','A','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','A','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','A','.','.'],
            ['.','.','.','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','.','.','.']
        ], self.default_test_antenna.antenna_map)
        self.assertEqual(2, len(self.default_test_antenna.antenna_frequency_list))
    
    def test_returns_antinode_positions_for_antennae(self):
        self.assertListEqual(
            [{'x': 3, 'y': 1}, {'x': 6, 'y': 7}],
            self.default_test_antenna.get_antinodes({'x': 4, 'y': 3}, {'x': 5, 'y': 5})
        )
        self.assertListEqual(
            [{'x': 0, 'y': 2}, {'x': 12, 'y': 5}],
            self.default_test_antenna.get_antinodes({'x': 4, 'y': 3}, {'x': 8, 'y': 4})
        )
        self.assertListEqual(
            [{'x': 11, 'y': 3}, {'x': 2, 'y': 6}],
            self.default_test_antenna.get_antinodes({'x': 8, 'y': 4}, {'x': 5, 'y': 5})
        )

if __name__ == "__main__":
    unittest.main()