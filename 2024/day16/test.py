import unittest
from maze_runner import MazeRunner

class TestMazeRunner(unittest.TestCase):
    
    first_example = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""
    example_row_length = 15
    expected_size = example_row_length*15
    start_position = (example_row_length * 13) + 1
    first_example_tile_position = (example_row_length * 2) + 1
    second_example_tile_position = (example_row_length * 3) + 1
    end_position = (example_row_length * 2) - 2
    
    first_example_path = """###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############"""

    second_example = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

    second_example_path = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################"""

    def test_it_parses_input_and_generates_adjacency_matrix_for_first_example(self):
        test_runner = MazeRunner(self.first_example)
        
        self.assertEqual(
            self.start_position, test_runner.start_position
        ) 
        self.assertEqual(
            self.end_position, test_runner.end_position
        )
        
        self.assertEqual(self.expected_size, len(test_runner.nodes))
        self.assertEqual('#', test_runner.nodes[0])
        self.assertEqual('E', test_runner.nodes[self.end_position])
        self.assertEqual('.', test_runner.nodes[self.first_example_tile_position])
        self.assertEqual('.', test_runner.nodes[self.second_example_tile_position])
        self.assertEqual('S', test_runner.nodes[self.start_position])
        
        self.assertEqual(self.expected_size, len(test_runner.maze_adjacency_matrix))
        #Walls arent adjacent to anything
        self.assertListEqual([0 for _ in range(self.expected_size)], test_runner.maze_adjacency_matrix[0])
        
        #The end is adjacent to two tiles
        expected_end_adjacencies = [0 for _ in range(self.expected_size)]
        expected_end_adjacencies[self.end_position - 1] = 1
        expected_end_adjacencies[self.end_position + self.example_row_length] = 1
        self.assertListEqual(expected_end_adjacencies, test_runner.maze_adjacency_matrix[self.end_position])
        
        #First example tile is adjacent to two 
        expected_first_tile_adjacencies = [0 for _ in range(self.expected_size)]
        expected_first_tile_adjacencies[self.first_example_tile_position - self.example_row_length] = 1
        expected_first_tile_adjacencies[self.first_example_tile_position + self.example_row_length] = 1
        self.assertListEqual(expected_first_tile_adjacencies, test_runner.maze_adjacency_matrix[self.first_example_tile_position])
        
        #Second example tile is adjacent to three 
        expected_second_tile_adjacencies = [0 for _ in range(self.expected_size)]
        expected_second_tile_adjacencies[self.second_example_tile_position - self.example_row_length] = 1
        expected_second_tile_adjacencies[self.second_example_tile_position + 1] = 1
        expected_second_tile_adjacencies[self.second_example_tile_position + self.example_row_length] = 1
        self.assertListEqual(expected_second_tile_adjacencies, test_runner.maze_adjacency_matrix[self.second_example_tile_position])
        
        #The start is adjacent to two tiles
        expected_start_adjacencies = [0 for _ in range(self.expected_size)]
        expected_start_adjacencies[self.start_position + 1] = 1
        expected_start_adjacencies[self.start_position - self.example_row_length] = 1
        self.assertListEqual(expected_start_adjacencies, test_runner.maze_adjacency_matrix[self.start_position])
    
    """def test_it_returns_the_best_path_for_first_example(self):
        test_runner = MazeRunner(self.first_example)
        self.assertEqual(self.first_example_path, test_runner.get_best_path())"""

    def test_it_returns_the_best_path_score_for_first_example(self):
        test_runner = MazeRunner(self.first_example)
        self.assertEqual(7036, test_runner.get_best_path_score())

    """def test_it_returns_the_best_path_score_for_second_example(self):
        test_runner = MazeRunner(self.first_example)
        self.assertEqual(11048, test_runner.get_best_path_score())"""

if __name__ == "__main__":
    unittest.main()