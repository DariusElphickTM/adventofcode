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

    test_dictionary = {
        190: [10, 19],
        3267: [81, 40, 27],
        83: [17, 5],
        156: [15, 6],
        7290: [6, 8, 6, 15],
        161011: [16, 10, 13],
        192: [17, 8, 14],
        21037: [9, 7, 18, 13],
        292: [11, 6, 16, 20],
    }
    
    def setUp(self):
        self.default_callibrator = callibrator.BridgeCallibrator(self.example_callibration_equations)
    
    def test_parses_callibration_equations_string(self):
        self.assertDictEqual({
            190: [10, 19],
            3267: [81, 40, 27],
            83: [17, 5],
            156: [15, 6],
            7290: [6, 8, 6, 15],
            161011: [16, 10, 13],
            192: [17, 8, 14],
            21037: [9, 7, 18, 13],
            292: [11, 6, 16, 20],
        }, self.default_callibrator.parse_callibration_string(self.example_callibration_equations))
    
    def test_should_find_correct_callibration_result_for_test_data(self):
        self.assertEqual(3749, self.default_callibrator.get_total_callibration())
    
    def test_should_return_true_for_callibrations_with_valid_solutions(self):
        self.assertTrue(self.default_callibrator.is_callibration_true(190, self.test_dictionary[190]))
        self.assertTrue(self.default_callibrator.is_callibration_true(3267, self.test_dictionary[3267]))
        self.assertTrue(self.default_callibrator.is_callibration_true(292, self.test_dictionary[292]))
    
    def test_should_return_false_for_callibrations_with_valid_solutions(self):
        self.assertFalse(self.default_callibrator.is_callibration_true(83, self.test_dictionary[83]))
        self.assertFalse(self.default_callibrator.is_callibration_true(156, self.test_dictionary[156]))
        self.assertFalse(self.default_callibrator.is_callibration_true(7290, self.test_dictionary[7290]))
        self.assertFalse(self.default_callibrator.is_callibration_true(161011, self.test_dictionary[161011]))
        self.assertFalse(self.default_callibrator.is_callibration_true(192, self.test_dictionary[192]))
        self.assertFalse(self.default_callibrator.is_callibration_true(21037, self.test_dictionary[21037]))

if __name__ == '__main__':
    unittest.main()