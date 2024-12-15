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
    
    def test_should_parse_input_string_with_second_example(self):
        test_defragger = defragger.Defragger("12345")
        self.assertListEqual(
            [
                '0','.','.','1','1','1','.','.','.','.','2','2','2','2','2'
            ], 
            test_defragger.disk_map
        )
    
    def test_should_defrag_disk(self):
        self.assertListEqual(
            [
                '0','0','9','9','8','1','1',
                '1','8','8','8','2','7','7',
                '7','3','3','3','6','4','4',
                '6','5','5','5','5','6','6',
                '.','.','.','.','.','.','.',
                '.','.','.','.','.','.','.'
            ],
            self.default_test_defragger.get_defragged_disk_map()
        )
    
    def test_should_defrag_disk_with_second_example(self):
        test_defragger = defragger.Defragger("12345")
        self.assertListEqual(
            [
                '0','2','2','1','1','1','2','2','2','.','.','.','.','.','.'
            ],
            test_defragger.get_defragged_disk_map()
        )

if __name__ == "__main__":
    unittest.main()