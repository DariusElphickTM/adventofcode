import unittest
import defragger

class TestDefragger(unittest.TestCase):
    
    test_string = """2333133121414131402"""
    
    def setUp(self):
        self.default_test_defragger = defragger.Defragger(self.test_string)
    
    def test_should_parse_input_string(self):
        self.assertListEqual(
            [
                '0','0','.','.','.','1','1',
                '1','.','.','.','2','.','.',
                '.','3','3','3','.','4','4',
                '.','5','5','5','5','.','6',
                '6','6','6','.','7','7','7',
                '.','8','8','8','8','9','9'
            ], 
            self.default_test_defragger.disk_map
        )

if __name__ == "__main__":
    unittest.main()