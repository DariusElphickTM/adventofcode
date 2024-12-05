import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_part_one(self):
        input_text = solution.read_file("input.txt")
        self.assertEqual(solution.part_one(input_text), 157621318)

if __name__ == "__main__":
    unittest.main()