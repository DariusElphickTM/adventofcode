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

    def test_it_returns_the_best_path_score_for_first_example(self):
        test_runner = MazeRunner(self.first_example)
        self.assertEqual(7036, test_runner.get_best_path_score())

    def test_it_returns_the_best_path_score_for_second_example(self):
        test_runner = MazeRunner(self.first_example)
        self.assertEqual(11048, test_runner.get_best_path_score())

if __name__ == "__main__":
    unittest.main()