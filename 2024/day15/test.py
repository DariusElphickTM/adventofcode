import unittest
from warehouse_watcher import WarehouseWatcher

class TestWarehouseWatcher(unittest.TestCase):
    
    small_example_input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
    
    example_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

    def test_it_should_parse_input_and_set_up_initial_warehouse_state_and_robot_moves(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        self.assertListEqual(
            ['<','^','^','>','>','>','v','v','<','v','>','>','v','<','<'],
            test_watcher.robot_moves
        )
        self.assertListEqual(
            [
                ['#','#','#','#','#','#','#','#'],
                ['#','.','.','O','.','O','.','#'],
                ['#','#','@','.','O','.','.','#'],
                ['#','.','.','.','O','.','.','#'],
                ['#','.','#','.','O','.','.','#'],
                ['#','.','.','.','O','.','.','#'],
                ['#','.','.','.','.','.','.','#'],
                ['#','#','#','#','#','#','#','#']
            ],
            test_watcher.current_warehouse_state
        )
        self.assertDictEqual({
            'x': 2,
            'y': 2
        }, test_watcher.current_robot_position)
    
    def test_it_should_not_move_if_wall_in_front(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('<')
        self.assertDictEqual({
            'x': 2,
            'y': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][2])
        
        test_watcher.play_move('^')
        test_watcher.play_move('^')
        self.assertDictEqual({
            'x': 2,
            'y': 1
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[1][2])
        
        test_watcher.play_move('v')
        test_watcher.play_move('v')
        test_watcher.play_move('v')
        self.assertDictEqual({
            'x': 2,
            'y': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][2])
    
    def test_it_should_play_a_move_when_next_position_is_empty(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('v')
        self.assertDictEqual({
            'x': 2,
            'y': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][2])
        self.assertEqual('.', test_watcher.current_warehouse_state[2][2])
        
        test_watcher.play_move('>')
        self.assertDictEqual({
            'x': 3,
            'y': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][3])
        self.assertEqual('.', test_watcher.current_warehouse_state[3][2])
        
        test_watcher.play_move('^')
        self.assertDictEqual({
            'x': 3,
            'y': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][3])
        self.assertEqual('.', test_watcher.current_warehouse_state[3][3])
        
        test_watcher.play_move('<')
        self.assertDictEqual({
            'x': 2,
            'y': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][2])
        self.assertEqual('.', test_watcher.current_warehouse_state[2][3])
    
    def test_it_returns_correct_gps_coordinate_sum_for_small_example(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_all_moves()
        self.assertEqual(2028, test_watcher.get_current_gps_sum())
    
    """def test_it_returns_correct_gps_coordinate_sum_for_example(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_all_moves()
        self.assertEqual(10092, test_watcher.get_current_gps_sum())"""

if __name__ == "__main__":
    unittest.main()