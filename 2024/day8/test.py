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

    test_bounds = {'x': 10, 'y': 10}
    
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
    
    def test_returns_correct_count_of_antinodes(self):
        self.assertEqual(
            14,
            self.default_test_antenna.get_antinode_count()
        )
    
    def test_returns_correct_count_of_antinodes_with_harmonics_count(self):
        self.default_test_antenna.with_harmonics = True
        self.assertEqual(
            34,
            self.default_test_antenna.get_antinode_count()
        )
        self.default_test_antenna.with_harmonics = False
    
    def test_returns_all_antinodes_for_frequency_with_harmonics(self):
        test_huge_antenna = huge_antenna.HugeAntenna("""T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........""")
        test_huge_antenna.with_harmonics = True
        self.assertListEqual([
                {'x': 0, 'y': 0},
                {'x': 3, 'y': 1},
                {'x': 6, 'y': 2},
                {'x': 9, 'y': 3},
                {'x': 0, 'y': 0},
                {'x': 1, 'y': 2},
                {'x': 2, 'y': 4},
                {'x': 3, 'y': 6},
                {'x': 4, 'y': 8},
                {'x': 3, 'y': 1},
                {'x': 5, 'y': 0},
                {'x': 1, 'y': 2}
            ], 
            test_huge_antenna.get_antinodes_for_frequency('T')
        )
        
    
    def test_returns_all_antinodes_for_frequency(self):
        self.assertListEqual([
                {'x': 4, 'y': 2},
                {'x': 10, 'y': 11},
                {'x': 3, 'y': 1},
                {'x': 7, 'y': 7},
                {'x': 10, 'y': 10}
            ], 
            self.default_test_antenna.get_antinodes_for_frequency('A')
        )
        
        self.assertListEqual([
                {'x': 11, 'y': 0},
                {'x': 2, 'y': 3},
                {'x': 6, 'y': 5},
                {'x': 0, 'y': 7},
                {'x': 3, 'y': 1},
                {'x': 9, 'y': 4},
                {'x': 6, 'y': 0},
                {'x': 3, 'y': 6},
                {'x': 10, 'y': 2},
                {'x': 1, 'y': 5}
            ], 
            self.default_test_antenna.get_antinodes_for_frequency('0')
        )
    
    def test_returns_all_antennae_matching_frequency(self):
        self.assertListEqual([
                {'x': 6, 'y': 5},
                {'x': 8, 'y': 8},
                {'x': 9, 'y': 9}
            ], 
            self.default_test_antenna.get_antennae_matching_frequency('A')
        )
        self.assertListEqual([
                {'x': 8, 'y': 1},
                {'x': 5, 'y': 2},
                {'x': 7, 'y': 3},
                {'x': 4, 'y': 4}
            ], 
            self.default_test_antenna.get_antennae_matching_frequency('0')
        )
    
    def test_returns_all_antinodes_for_antenna_frequency(self):
        self.assertListEqual([
                {'x': 3, 'y': 1}, 
                {'x': 6, 'y': 7},
                {'x': 0, 'y': 2},
                {'x': 2, 'y': 6}
            ], 
            self.default_test_antenna.get_antinodes_for_antennae([
                {'x': 4, 'y': 3}, {'x': 5, 'y': 5}, {'x': 8, 'y': 4}
            ], self.test_bounds)
        )
    
    def test_returns_antinodes_after_filtering_out_ones_out_of_bounds(self):
        self.assertListEqual(
            [{'x': 3, 'y': 1}, {'x': 6, 'y': 7}],
            self.default_test_antenna.get_antinodes_within_bounds({'x': 4, 'y': 3}, {'x': 5, 'y': 5}, self.test_bounds)
        )
        self.assertListEqual(
            [{'x': 0, 'y': 2}],
            self.default_test_antenna.get_antinodes_within_bounds({'x': 4, 'y': 3}, {'x': 8, 'y': 4}, self.test_bounds)
        )
        self.assertListEqual(
            [{'x': 2, 'y': 6}],
            self.default_test_antenna.get_antinodes_within_bounds({'x': 8, 'y': 4}, {'x': 5, 'y': 5}, self.test_bounds)
        )
    
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