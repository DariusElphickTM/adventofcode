import unittest
from defragger import Defragger

class TestDefragger(unittest.TestCase):
    
    test_string = """2333133121414131402"""
    
    def setUp(self):
        self.default_test_defragger = Defragger(self.test_string)
    
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
    
    def test_should_parse_input_string_into_block_map(self):
        self.assertListEqual(
            [
                {
                    'id': '0',
                    'size': 2
                },
                {
                    'id': '.',
                    'size': 3
                },
                {
                    'id': '1',
                    'size': 3
                },
                {
                    'id': '.',
                    'size': 3
                },
                {
                    'id': '2',
                    'size': 1
                },
                {
                    'id': '.',
                    'size': 3
                },
                {
                    'id': '3',
                    'size': 3
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '4',
                    'size': 2
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '5',
                    'size': 4
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '6',
                    'size': 4
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '7',
                    'size': 3
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '8',
                    'size': 4
                },
                {
                    'id': '9',
                    'size': 2
                }
            ], 
            self.default_test_defragger.disk_block_map
        )
    
    def test_should_parse_input_string_with_second_example(self):
        test_defragger = Defragger("12345")
        self.assertListEqual(
            [
                '0','.','.','1','1','1','.','.','.','.','2','2','2','2','2'
            ], 
            test_defragger.disk_map
        )
    
    def test_should_parse_input_string_into_block_map_for_second_example(self):
        test_defragger = Defragger("12345")
        self.assertListEqual(
            [
                {
                    'id': '0',
                    'size': 1
                },
                {
                    'id': '.',
                    'size': 2
                },
                {
                    'id': '1',
                    'size': 3
                },
                {
                    'id': '.',
                    'size': 4
                },
                {
                    'id': '2',
                    'size': 5
                }
            ], 
            test_defragger.disk_block_map
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
            self.default_test_defragger.get_defragged_disk_map_simple_mode()
        )
    
    def test_should_defrag_disk_with_second_example(self):
        test_defragger = Defragger("12345")
        self.assertListEqual(
            [
                '0','2','2','1','1','1','2','2','2','.','.','.','.','.','.'
            ],
            test_defragger.get_defragged_disk_map_simple_mode()
        )
    
    def test_should_get_file_system_checksum(self):
        self.assertEqual(
            1928,
            self.default_test_defragger.get_file_system_checksum()
        )
    
    def test_should_get_file_system_checksum_in_whole_file_mode(self):
        test_defragger = Defragger(self.test_string, True)
        self.assertEqual(
            2858,
            test_defragger.get_file_system_checksum()
        )
    
    def test_should_defrag_disk_in_whole_file_mode(self):
        test_defragger = Defragger(self.test_string, True)
        self.assertListEqual(
            [
                {
                    'id': '0',
                    'size': 2
                },
                {
                    'id': '9',
                    'size': 2
                },
                {
                    'id': '2',
                    'size': 1
                },
                {
                    'id': '1',
                    'size': 3
                },
                {
                    'id': '7',
                    'size': 3
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '4',
                    'size': 2
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '3',
                    'size': 3
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '.',
                    'size': 2
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '5',
                    'size': 4
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '6',
                    'size': 4
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '.',
                    'size': 3
                },
                {
                    'id': '.',
                    'size': 1
                },
                {
                    'id': '8',
                    'size': 4
                },
                {
                    'id': '.',
                    'size': 2
                }
            ],
            test_defragger.get_defragged_disk_map_whole_file_mode()
        )

if __name__ == "__main__":
    unittest.main()