import unittest
from stone_observer import StoneObserver  

class TestStoneObserver(unittest.TestCase):
    
    example_input = """125 17"""
    
    def setUp(self):
        self.default_stone_observer = StoneObserver(self.example_input)
    
    def test_should_return_current_stone_count(self):
        self.assertEqual(self.default_stone_observer.get_stone_count(), 2)
    
    def test_should_return_current_stones(self):
        self.assertListEqual(["125", "17"], self.default_stone_observer.get_current_stones())
    
    def test_should_return_correct_current_stones_for_example_output(self):
        self.default_stone_observer.blink(5)
        self.default_stone_observer.print_tree(self.default_stone_observer.stones_tree)
        self.assertEqual(self.default_stone_observer.get_stone_count(), 5342)

if __name__ == "__main__":
    unittest.main()