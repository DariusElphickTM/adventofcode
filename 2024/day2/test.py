import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_positive_safe(self):
        self.assertTrue(solution.checkSafety("1 2 3 4 5\n"))
        self.assertTrue(solution.checkSafety("1 2 3 4 5 6 7 8 9 10\n"))
        self.assertTrue(solution.checkSafety("2 3 4 5 6\n"))
        self.assertTrue(solution.checkSafety("1 3 4 5 6\n"))
        self.assertTrue(solution.checkSafety("1 4 5 6 7\n"))
        self.assertTrue(solution.checkSafety("1 2 4 5 6\n"))
        self.assertTrue(solution.checkSafety("1 2 3 5 6\n"))
        self.assertTrue(solution.checkSafety("1 2 3 4 6\n"))
        self.assertTrue(solution.checkSafety("11 12 13 14 16\n"))
        self.assertTrue(solution.checkSafety("111 112 113 114 116\n"))
    
    def test_negative_safe(self):
        self.assertTrue(solution.checkSafety("5 4 3 2 1\n"))
        self.assertTrue(solution.checkSafety("10 9 8 7 6 5 4 3 2 1\n"))
        self.assertTrue(solution.checkSafety("6 5 4 3 2\n"))
        self.assertTrue(solution.checkSafety("6 5 4 3 1\n"))
        self.assertTrue(solution.checkSafety("7 6 5 4 1\n"))
        self.assertTrue(solution.checkSafety("6 5 4 2 1\n"))
        self.assertTrue(solution.checkSafety("6 5 3 2 1\n"))
        self.assertTrue(solution.checkSafety("6 4 3 2 1\n"))
        self.assertTrue(solution.checkSafety("16 14 13 12 11\n"))
        self.assertTrue(solution.checkSafety("116 114 113 112 111\n"))
    
    def test_unsafe_level_order(self):
        self.assertFalse(solution.checkSafety("1 4 3 4 5\n"))
        self.assertFalse(solution.checkSafety("5 2 3 2 1\n"))
    
    def test_unsafe_level_difference(self):
        self.assertFalse(solution.checkSafety("1 5 6 7 8\n"))
        self.assertFalse(solution.checkSafety("1 4 3 4 20\n"))
        self.assertFalse(solution.checkSafety("8 4 3 2 1\n"))
    
    def test_part_two_positive_safe(self):
        self.assertTrue(solution.checkSafety("1 2 3 4 5\n"), True)
        self.assertTrue(solution.checkSafety("1 2 3 4 5 6 7 8 9 10\n", True))
        self.assertTrue(solution.checkSafety("2 3 4 5 6\n", True))
        self.assertTrue(solution.checkSafety("1 3 4 5 6\n", True))
        self.assertTrue(solution.checkSafety("1 4 5 6 7\n", True))
        self.assertTrue(solution.checkSafety("1 2 4 5 6\n", True))
        self.assertTrue(solution.checkSafety("1 2 3 5 6\n", True))
        self.assertTrue(solution.checkSafety("1 2 3 4 6\n", True))
        self.assertTrue(solution.checkSafety("11 12 13 14 16\n", True))
        self.assertTrue(solution.checkSafety("111 112 113 114 116\n", True))
    
    def test_part_two_negative_safe(self):
        self.assertTrue(solution.checkSafety("5 4 3 2 1\n", True))
        self.assertTrue(solution.checkSafety("10 9 8 7 6 5 4 3 2 1\n", True))
        self.assertTrue(solution.checkSafety("6 5 4 3 2\n", True))
        self.assertTrue(solution.checkSafety("6 5 4 3 1\n", True))
        self.assertTrue(solution.checkSafety("7 6 5 4 1\n", True))
        self.assertTrue(solution.checkSafety("6 5 4 2 1\n", True))
        self.assertTrue(solution.checkSafety("6 5 3 2 1\n", True))
        self.assertTrue(solution.checkSafety("6 4 3 2 1\n", True))
        self.assertTrue(solution.checkSafety("16 14 13 12 11\n", True))
        self.assertTrue(solution.checkSafety("116 114 113 112 111\n", True))
    
    def test_part_two_safe_edge_cases(self):
        self.assertTrue(solution.checkSafety("48 46 47 49 51 54 56\n", True))
        self.assertTrue(solution.checkSafety("1 1 2 3 4 5\n", True))
        self.assertTrue(solution.checkSafety("1 2 3 4 5 5\n", True))
        self.assertTrue(solution.checkSafety("5 1 2 3 4 5\n", True))
        self.assertTrue(solution.checkSafety("1 4 3 2 1\n", True))
        self.assertTrue(solution.checkSafety("1 6 7 8 9\n", True))
        self.assertTrue(solution.checkSafety("1 2 3 4 3\n", True))
        self.assertTrue(solution.checkSafety("9 8 7 6 7\n", True))
        self.assertTrue(solution.checkSafety("7 10 8 10 11\n", True))
        self.assertTrue(solution.checkSafety("29 28 27 25 26 25 22 20\n", True))
    
    def test_part_two_unsafe_edge_cases(self):
        self.assertTrue(solution.checkSafety("48 55 47 49 51 54 56\n", True))
        self.assertTrue(solution.checkSafety("1 1 1 3 4 5\n", True))
        self.assertTrue(solution.checkSafety("1 2 3 4 5 5 5\n", True))
        self.assertTrue(solution.checkSafety("5 1 2 3 4 55\n", True))
        
    def test_part_1_safe_count(self):
        reports = solution.readFile("1.txt")
        self.assertEqual(solution.process_reports(reports).count(True), 549)

if __name__ == "__main__":
    unittest.main()