import unittest
import guard_gallivant

class TestGuardGallivant(unittest.TestCase):
    test_map = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    def setUp(self):
        self.default_test_gallivanter = guard_gallivant.GuardGallivant(self.test_map) 
    
    def test_setup_map_parses_map_correctly(self):
        room_map = self.default_test_gallivanter.room_map
        self.assertListEqual([
            ['.','.','.','.','#','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','.','#'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','.','#','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','#','.','.'],
            ['.','.','.','.','.','.','.','.','.','.'],
            ['.','#','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','.','.','#','.'],
            ['#','.','.','.','.','.','.','.','.','.'],
            ['.','.','.','.','.','.','#','.','.','.']
        ], room_map)
        
        guard = self.default_test_gallivanter.guard
        self.assertDictEqual(
            {'x': 4, 'y': 6, 'facing': '^'},
            guard
        )
    
    def test_to_string_method(self):
        self.assertEqual("""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""", str(self.default_test_gallivanter))

if __name__ == "__main__":
    unittest.main()