import unittest
import solution

class TestSolution(unittest.TestCase):
    
    def test_parse_ordering_rules_correctly(self):
        sample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13"""
        result = solution.parse_rules(sample)
        self.assertDictEqual({
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13],
        }, result)
    
    def test_parse_updates_correctly(self):
        sample = """75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
        result = solution.parse_updates(sample)
        self.assertEqual(len(result), 6)
        self.assertEqual(len(result[0]), 5)
        self.assertEqual(result[0][0], 75)
        self.assertEqual(result[0][2], 61)
        self.assertEqual(result[0][4], 29)
        self.assertEqual(len(result[2]), 3)
        

if __name__ == "__main__":
    unittest.main()