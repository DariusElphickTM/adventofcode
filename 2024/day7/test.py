import unittest
import callibrator

class TestBridgeCallibrator(unittest.TestCase):
    
    example_callibration_equations = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

    test_list = [
        {'callibration_result': 190, 'callibration_steps': [10, 19]},
        {'callibration_result': 3267, 'callibration_steps': [81, 40, 27]},
        {'callibration_result': 83, 'callibration_steps': [17, 5]},
        {'callibration_result': 156, 'callibration_steps': [15, 6]},
        {'callibration_result': 7290, 'callibration_steps': [6, 8, 6, 15]},
        {'callibration_result': 161011, 'callibration_steps': [16, 10, 13]},
        {'callibration_result': 192, 'callibration_steps': [17, 8, 14]},
        {'callibration_result': 21037, 'callibration_steps': [9, 7, 18, 13]},
        {'callibration_result': 292, 'callibration_steps': [11, 6, 16, 20]},
    ]
    
    def setUp(self):
        self.default_callibrator = callibrator.BridgeCallibrator(self.example_callibration_equations)
    
    def test_parses_callibration_equations_string(self):
        self.assertListEqual(self.test_list, self.default_callibrator.parse_callibration_string(self.example_callibration_equations))
    
    def test_should_find_correct_callibration_result_for_test_data(self):
        self.assertEqual(3749, self.default_callibrator.get_total_callibration())
    
    def test_should_give_expected_result_with_more_test_data(self):
        test_callibrator = callibrator.BridgeCallibrator("""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
108: 4 5 3 9
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
108: 2 2 5 12""")
        self.assertEqual(3965, test_callibrator.get_total_callibration())
    
    def test_should_return_true_for_callibrations_with_valid_solutions(self):
        self.assertTrue(self.default_callibrator.is_callibration_true(190, self.test_list[0]['callibration_steps']))
        self.assertTrue(self.default_callibrator.is_callibration_true(3267, self.test_list[1]['callibration_steps']))
        self.assertTrue(self.default_callibrator.is_callibration_true(292, self.test_list[8]['callibration_steps']))
    
    def test_should_return_false_for_callibrations_with_valid_solutions(self):
        self.assertFalse(self.default_callibrator.is_callibration_true(83, self.test_list[2]['callibration_steps']))
        self.assertFalse(self.default_callibrator.is_callibration_true(156, self.test_list[3]['callibration_steps']))
        self.assertFalse(self.default_callibrator.is_callibration_true(7290, self.test_list[4]['callibration_steps']))
        self.assertFalse(self.default_callibrator.is_callibration_true(161011, self.test_list[5]['callibration_steps']))
        self.assertFalse(self.default_callibrator.is_callibration_true(192, self.test_list[6]['callibration_steps']))
        self.assertFalse(self.default_callibrator.is_callibration_true(21037, self.test_list[7]['callibration_steps']))

if __name__ == '__main__':
    unittest.main()