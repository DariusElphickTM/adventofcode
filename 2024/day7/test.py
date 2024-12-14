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

if __name__ == '__main__':
    unittest.main()