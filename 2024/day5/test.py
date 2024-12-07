import unittest
import print_inspector

class TestSolution(unittest.TestCase):
    test_data = """47|53
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
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    test_rules = test_data.split("\n\n", maxsplit=1)[0]
    test_updates = test_data.split("\n\n")[1]
    
    def setUp(self):
        self.default_test_inspector = print_inspector.PrintInspector(self.test_rules)
    
    def test_get_part_1_answer(self):
        self.assertEqual(self.default_test_inspector.get_part_1_answer(self.test_updates), 143)
    
    def test_find_safe_updates_returns_correct_entries(self):
        test_result = self.default_test_inspector.find_safe_updates(self.test_updates)
        self.assertListEqual(test_result, [
            [75,47,61,53,29],
            [97,61,53,29,13],
            [75,29,13]
        ])
    
    def test_is_safe_returns_true_for_safe_updates(self):
        parsed_test_updates = self.default_test_inspector.parse_updates(self.test_updates)
        self.assertTrue(self.default_test_inspector.is_update_safe(parsed_test_updates[0]))
        self.assertTrue(self.default_test_inspector.is_update_safe(parsed_test_updates[1]))
        self.assertTrue(self.default_test_inspector.is_update_safe(parsed_test_updates[2]))
    
    def test_is_safe_returns_false_for_unsafe_updates(self):
        parsed_test_updates = self.default_test_inspector.parse_updates(self.test_updates)
        self.assertFalse(self.default_test_inspector.is_update_safe(parsed_test_updates[3]))
        self.assertFalse(self.default_test_inspector.is_update_safe(parsed_test_updates[4]))
        self.assertFalse(self.default_test_inspector.is_update_safe(parsed_test_updates[5]))

    def test_parse_ordering_rules_correctly(self):
        self.assertDictEqual({
            47: [53, 13, 61, 29],
            97: [13, 61, 47, 29, 53, 75],
            75: [29, 53, 47, 61, 13],
            61: [13, 53, 29],
            29: [13],
            53: [29, 13],
        }, self.default_test_inspector.rules)
    
    def test_parse_updates_correctly(self):
        result = self.default_test_inspector.parse_updates(self.test_updates)
        self.assertEqual(len(result), 6)
        self.assertEqual(len(result[0]), 5)
        self.assertEqual(result[0][0], 75)
        self.assertEqual(result[0][2], 61)
        self.assertEqual(result[0][4], 29)
        self.assertEqual(len(result[2]), 3)

if __name__ == "__main__":
    unittest.main()