import unittest
from warehouse_watcher import WarehouseWatcher, BigWarehouseWatcher

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
            'y': 2,
            'x': 2
        }, test_watcher.current_robot_position)
    
    def test_it_should_play_all_robot_moves_and_return_the_right_state_for_small_example(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_all_moves()
        self.assertListEqual(
            [
                ['#','#','#','#','#','#','#','#'],
                ['#','.','.','.','.','O','O','#'],
                ['#','#','.','.','.','.','.','#'],
                ['#','.','.','.','.','.','O','#'],
                ['#','.','#','O','@','.','.','#'],
                ['#','.','.','.','O','.','.','#'],
                ['#','.','.','.','O','.','.','#'],
                ['#','#','#','#','#','#','#','#']
            ],
            test_watcher.current_warehouse_state
        )
    
    def test_it_should_play_all_robot_moves_and_return_the_right_state_for_example(self):
        test_watcher = WarehouseWatcher(self.example_input)
        test_watcher.play_all_moves()
        self.assertListEqual(
            [
                ['#','#','#','#','#','#','#','#','#','#'],
                ['#','.','O','.','O','.','O','O','O','#'],
                ['#','.','.','.','.','.','.','.','.','#'],
                ['#','O','O','.','.','.','.','.','.','#'],
                ['#','O','O','@','.','.','.','.','.','#'],
                ['#','O','#','.','.','.','.','.','O','#'],
                ['#','O','.','.','.','.','.','O','O','#'],
                ['#','O','.','.','.','.','.','O','O','#'],
                ['#','O','O','.','.','.','.','O','O','#'],
                ['#','#','#','#','#','#','#','#','#','#']
            ],
            test_watcher.current_warehouse_state
        )
    
    def test_it_wont_push_a_single_block_when_there_is_a_wall_in_the_way(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('>')
        test_watcher.play_move('^')
        self.assertDictEqual({
            'y': 2,
            'x': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][3])
        self.assertEqual('O', test_watcher.current_warehouse_state[2][4])
    
    def test_it_wont_push_multiple_blocks_when_there_is_a_wall_in_the_way(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('>')
        test_watcher.play_move('>')
        self.assertDictEqual({
            'y': 2,
            'x': 4
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[2][5])
        
        test_watcher.play_move('v')
        test_watcher.play_move('v')
        self.assertDictEqual({
            'y': 3,
            'x': 4
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[4][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[5][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[6][4])
    
    def test_it_can_push_multiple_blocks_when_no_wall_in_the_way(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('>')
        test_watcher.play_move('>')
        self.assertDictEqual({
            'y': 2,
            'x': 4
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[2][5])
        
        test_watcher.play_move('v')
        self.assertDictEqual({
            'y': 3,
            'x': 4
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[4][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[5][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[6][4])
    
    def test_it_can_push_a_single_block_when_no_wall_in_the_way(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('>')
        test_watcher.play_move('>')
        self.assertDictEqual({
            'y': 2,
            'x': 4
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[2][5])
        
        test_watcher.play_move('^')
        test_watcher.play_move('<')
        self.assertDictEqual({
            'y': 1,
            'x': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[1][3])
        self.assertEqual('O', test_watcher.current_warehouse_state[1][2])
    
    def test_it_wont_move_if_wall_in_front_of_robot(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('<')
        self.assertDictEqual({
            'y': 2,
            'x': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][2])
        
        test_watcher.play_move('^')
        test_watcher.play_move('^')
        self.assertDictEqual({
            'y': 1,
            'x': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[1][2])
        
        test_watcher.play_move('v')
        test_watcher.play_move('v')
        test_watcher.play_move('v')
        self.assertDictEqual({
            'y': 3,
            'x': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][2])
    
    def test_it_should_play_a_move_when_next_position_is_empty(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('v')
        self.assertDictEqual({
            'y': 3,
            'x': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][2])
        self.assertEqual('.', test_watcher.current_warehouse_state[2][2])
        
        test_watcher.play_move('>')
        self.assertDictEqual({
            'y': 3,
            'x': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][3])
        self.assertEqual('.', test_watcher.current_warehouse_state[3][2])
        
        test_watcher.play_move('^')
        self.assertDictEqual({
            'y': 2,
            'x': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][3])
        self.assertEqual('.', test_watcher.current_warehouse_state[3][3])
        
        test_watcher.play_move('<')
        self.assertDictEqual({
            'y': 2,
            'x': 2
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][2])
        self.assertEqual('.', test_watcher.current_warehouse_state[2][3])
    
    def test_it_returns_correct_gps_coordinate_sum_for_small_example(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_all_moves()
        self.assertEqual(2028, test_watcher.get_current_gps_sum())
    
    def test_it_returns_correct_gps_coordinate_sum_for_example(self):
        test_watcher = WarehouseWatcher(self.example_input)
        test_watcher.play_all_moves()
        self.assertEqual(10092, test_watcher.get_current_gps_sum())

class TestBigWarehouseWatcher(unittest.TestCase):
    
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

    def play_move_sequence(self, watcher, move_sequence):
        for move in move_sequence:
            watcher.play_move(move)
    
    def assert_box_at_position(self, watcher, position):
        self.assertEqual('[', watcher.current_warehouse_state[position['y']][position['x']])
        self.assertEqual(']', watcher.current_warehouse_state[position['y']][position['x'] + 1])
    
    def assert_robot_at_position(self, watcher, postion):
        self.assertDictEqual(postion, watcher.current_robot_position)
        self.assertEqual('@', watcher.current_warehouse_state[postion['y']][postion['x']])

    def test_it_should_parse_input_and_set_up_initial_warehouse_state_and_robot_moves_for_example(self):
        test_watcher = BigWarehouseWatcher(self.example_input)
        self.assertEqual(709, len(test_watcher.robot_moves))
        self.assertListEqual(
            [
                ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                ['#','#','.','.','.','.','[',']','.','.','.','.','[',']','.','.','[',']','#','#'],
                ['#','#','.','.','.','.','.','.','.','.','.','.','.','.','[',']','.','.','#','#'],
                ['#','#','.','.','[',']','[',']','.','.','.','.','[',']','.','.','[',']','#','#'],
                ['#','#','.','.','.','.','[',']','@','.','.','.','.','.','[',']','.','.','#','#'],
                ['#','#','[',']','#','#','.','.','.','.','[',']','.','.','.','.','.','.','#','#'],
                ['#','#','[',']','.','.','.','.','[',']','.','.','.','.','[',']','.','.','#','#'],
                ['#','#','.','.','[',']','[',']','.','.','[',']','.','.','[',']','[',']','#','#'],
                ['#','#','.','.','.','.','.','.','.','.','[',']','.','.','.','.','.','.','#','#'],
                ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']
            ],
            test_watcher.current_warehouse_state
        )
        self.assertDictEqual({
            'y': 4,
            'x': 8
        }, test_watcher.current_robot_position)

    def test_it_should_parse_input_and_set_up_initial_warehouse_state_and_robot_moves_for_small_example(self):
        test_watcher = BigWarehouseWatcher(self.small_example_input)
        self.assertEqual(15, len(test_watcher.robot_moves))
        self.assertListEqual(
            [
                ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                ['#','#','.','.','.','.','[',']','.','.','[',']','.','.','#','#'],
                ['#','#','#','#','@','.','.','.','[',']','.','.','.','.','#','#'],
                ['#','#','.','.','.','.','.','.','[',']','.','.','.','.','#','#'],
                ['#','#','.','.','#','#','.','.','[',']','.','.','.','.','#','#'],
                ['#','#','.','.','.','.','.','.','[',']','.','.','.','.','#','#'],
                ['#','#','.','.','.','.','.','.','.','.','.','.','.','.','#','#'],
                ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
            ],
            test_watcher.current_warehouse_state
        )
        self.assert_robot_at_position(test_watcher, {'y': 2, 'x': 4})
    
    def test_it_can_push_a_single_block_when_no_wall_in_the_way(self):
        test_watcher = BigWarehouseWatcher(self.small_example_input)
        self.play_move_sequence(test_watcher, ['>','>','>','>'])
        self.assert_robot_at_position(test_watcher, {'y': 2, 'x': 8})
        self.assert_box_at_position(test_watcher, {'y': 2, 'x': 9})
        
        self.play_move_sequence(test_watcher, ['>','>'])
        self.assert_robot_at_position(test_watcher, {'y': 2, 'x': 10})
        self.assert_box_at_position(test_watcher, {'y': 2, 'x': 11})
        
        self.play_move_sequence(test_watcher, ['v','<'])
        self.assert_robot_at_position(test_watcher, {'y': 3, 'x': 9})
        self.assert_box_at_position(test_watcher, {'y': 3, 'x': 7})
        
        self.play_move_sequence(test_watcher, ['<','^','<','v'])
        self.assert_robot_at_position(test_watcher, {'y': 3, 'x': 7})
        self.assert_box_at_position(test_watcher, {'y': 4, 'x': 6})
        
        self.play_move_sequence(test_watcher, ['^','>','>','>','>','v','>','^'])
        self.assert_robot_at_position(test_watcher, {'y': 2, 'x': 12})
        self.assert_box_at_position(test_watcher, {'y': 1, 'x': 12})
    
    def test_it_should_play_a_move_when_next_position_is_empty(self):
        test_watcher = BigWarehouseWatcher(self.small_example_input)
        test_watcher.play_move('>')
        self.assert_robot_at_position(test_watcher, {'y': 2, 'x': 5})
        self.assertEqual('.', test_watcher.current_warehouse_state[2][4])
        
        test_watcher.play_move('v')
        self.assert_robot_at_position(test_watcher, {'y': 3, 'x': 5})
        self.assertEqual('.', test_watcher.current_warehouse_state[2][5])
        
        test_watcher.play_move('<')
        self.assert_robot_at_position(test_watcher, {'y': 3, 'x': 4})
        self.assertEqual('.', test_watcher.current_warehouse_state[3][5])
        
        test_watcher.play_move('^')
        self.assert_robot_at_position(test_watcher, {'y': 2, 'x': 4})
        self.assertEqual('.', test_watcher.current_warehouse_state[3][4])
    
    def test_it_wont_move_if_wall_in_front_of_robot(self):
        test_watcher = BigWarehouseWatcher(self.small_example_input)
        test_watcher.play_move('<')
        self.assert_robot_at_position(test_watcher, {'y': 2, 'x': 4})
        
        self.play_move_sequence(test_watcher, ['^','^'])
        self.assert_robot_at_position(test_watcher, {'y': 1, 'x': 4})
        
        self.play_move_sequence(test_watcher, ['v','v','v'])
        self.assert_robot_at_position(test_watcher, {'y': 3, 'x': 4})

    """
    
    def test_it_should_play_all_robot_moves_and_return_the_right_state_for_small_example(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_all_moves()
        self.assertListEqual(
            [
                ['#','#','#','#','#','#','#','#'],
                ['#','.','.','.','.','O','O','#'],
                ['#','#','.','.','.','.','.','#'],
                ['#','.','.','.','.','.','O','#'],
                ['#','.','#','O','@','.','.','#'],
                ['#','.','.','.','O','.','.','#'],
                ['#','.','.','.','O','.','.','#'],
                ['#','#','#','#','#','#','#','#']
            ],
            test_watcher.current_warehouse_state
        )
    
    def test_it_should_play_all_robot_moves_and_return_the_right_state_for_example(self):
        test_watcher = WarehouseWatcher(self.example_input)
        test_watcher.play_all_moves()
        self.assertListEqual(
            [
                ['#','#','#','#','#','#','#','#','#','#'],
                ['#','.','O','.','O','.','O','O','O','#'],
                ['#','.','.','.','.','.','.','.','.','#'],
                ['#','O','O','.','.','.','.','.','.','#'],
                ['#','O','O','@','.','.','.','.','.','#'],
                ['#','O','#','.','.','.','.','.','O','#'],
                ['#','O','.','.','.','.','.','O','O','#'],
                ['#','O','.','.','.','.','.','O','O','#'],
                ['#','O','O','.','.','.','.','O','O','#'],
                ['#','#','#','#','#','#','#','#','#','#']
            ],
            test_watcher.current_warehouse_state
        )
    
    def test_it_wont_push_a_single_block_when_there_is_a_wall_in_the_way(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('>')
        test_watcher.play_move('^')
        self.assertDictEqual({
            'y': 2,
            'x': 3
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][3])
        self.assertEqual('O', test_watcher.current_warehouse_state[2][4])
    
    def test_it_wont_push_multiple_blocks_when_there_is_a_wall_in_the_way(self):
        test_watcher = WarehouseWatcher(self.small_example_input)
        test_watcher.play_move('>')
        test_watcher.play_move('>')
        self.assertDictEqual({
            'y': 2,
            'x': 4
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[2][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[2][5])
        
        test_watcher.play_move('v')
        test_watcher.play_move('v')
        self.assertDictEqual({
            'y': 3,
            'x': 4
        }, test_watcher.current_robot_position)
        self.assertEqual('@', test_watcher.current_warehouse_state[3][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[4][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[5][4])
        self.assertEqual('O', test_watcher.current_warehouse_state[6][4])
    
    
    
"""
    
    """def test_it_returns_correct_gps_coordinate_sum_for_small_example(self):
        test_watcher = BigWarehouseWatcher(self.small_example_input)
        test_watcher.play_all_moves()
        self.assertEqual(2028, test_watcher.get_current_gps_sum())"""
    
    def test_it_returns_correct_gps_coordinate_sum_for_example(self):
        test_watcher = BigWarehouseWatcher(self.example_input)
        test_watcher.play_all_moves()
        self.assertEqual(9021, test_watcher.get_current_gps_sum())

if __name__ == "__main__":
    unittest.main()