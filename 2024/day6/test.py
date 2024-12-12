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
    
    def test_get_guards_next_position(self):
        self.assertDictEqual(
            {'x': 4, 'y': 5, 'facing': '^'}, self.default_test_gallivanter.get_guards_next_position({'x': 4, 'y': 6, 'facing': '^'})
        )
        self.assertDictEqual(
            {'x': 4, 'y': 7, 'facing': 'v'}, self.default_test_gallivanter.get_guards_next_position({'x': 4, 'y': 6, 'facing': 'v'})
        )
        self.assertDictEqual(
            {'x': 3, 'y': 6, 'facing': '<'}, self.default_test_gallivanter.get_guards_next_position({'x': 4, 'y': 6, 'facing': '<'})
        )
        self.assertDictEqual(
            {'x': 5, 'y': 6, 'facing': '>'}, self.default_test_gallivanter.get_guards_next_position({'x': 4, 'y': 6, 'facing': '>'})
        )
    
    def test_should_play_the_game(self):
        self.default_test_gallivanter.play()
        self.assertEqual(41, self.default_test_gallivanter.step_count)
    
    def test_should_turn_guard(self):
        self.assertEqual({'x': 4, 'y': 6, 'facing': '>'}, self.default_test_gallivanter.turn_guard({'x': 4, 'y': 6, 'facing': '^'}))
        self.assertEqual({'x': 4, 'y': 6, 'facing': 'v'}, self.default_test_gallivanter.turn_guard({'x': 4, 'y': 6, 'facing': '>'}))
        self.assertEqual({'x': 4, 'y': 6, 'facing': '<'}, self.default_test_gallivanter.turn_guard({'x': 4, 'y': 6, 'facing': 'v'}))
        self.assertEqual({'x': 4, 'y': 6, 'facing': '^'}, self.default_test_gallivanter.turn_guard({'x': 4, 'y': 6, 'facing': '<'}))
    
    def test_should_detect_when_guard_out_of_bounds(self):
        self.assertTrue(self.default_test_gallivanter.guard_out_of_bounds({'x': 4, 'y': -1, 'facing': '^'}))
        self.assertTrue(self.default_test_gallivanter.guard_out_of_bounds({'x': 4, 'y': 10, 'facing': 'v'}))
        self.assertTrue(self.default_test_gallivanter.guard_out_of_bounds({'x': -1, 'y': 6, 'facing': '<'}))
        self.assertTrue(self.default_test_gallivanter.guard_out_of_bounds({'x': 10, 'y': 6, 'facing': '>'}))
        self.assertFalse(self.default_test_gallivanter.guard_out_of_bounds({'x': 4, 'y': 6, 'facing': '^'}))
        self.assertFalse(self.default_test_gallivanter.guard_out_of_bounds({'x': 0, 'y': 9, 'facing': 'v'}))
        self.assertFalse(self.default_test_gallivanter.guard_out_of_bounds({'x': 9, 'y': 0, 'facing': '<'}))

if __name__ == "__main__":
    unittest.main()