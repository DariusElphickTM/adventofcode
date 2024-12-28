import unittest
from stone_observer import StoneObserver, MultiThreadedStoneObserver, DictionaryStoneObserver  

class TestStoneObserver(unittest.TestCase):
    
    example_input = """125 17"""
    
    def setUp(self):
        self.default_stone_observer = StoneObserver(self.example_input)
    
    def test_should_return_current_stone_count(self):
        self.assertEqual(self.default_stone_observer.get_stone_count(), 2)
    
    def test_should_return_current_stones(self):
        self.assertListEqual(["125", "17"], self.default_stone_observer.get_current_stones())
    
    def test_should_return_correct_current_stones_for_example_output_in_6_blinks(self):
        test_stone_observer = StoneObserver(self.example_input)
        test_stone_observer.blink()
        self.assertListEqual(["253000", "1", "7"], test_stone_observer.get_current_stones())
        test_stone_observer.blink()
        self.assertListEqual(["253", "0", "2024", "14168"], test_stone_observer.get_current_stones())
        test_stone_observer.blink()
        self.assertListEqual(["512072", "1", "20", "24", "28676032"], test_stone_observer.get_current_stones())
        test_stone_observer.blink()
        self.assertListEqual(["512", "72", "2024", "2", "0", "2", "4", "2867", "6032"], test_stone_observer.get_current_stones())
        test_stone_observer.blink()
        self.assertListEqual(["1036288", "7", "2", "20", "24", "4048", "1", "4048", "8096", "28", "67", "60", "32"], test_stone_observer.get_current_stones())
        test_stone_observer.blink()
        self.assertListEqual(["2097446912", "14168", "4048", "2", "0", "2", "4", "40", "48", "2024", "40", "48", "80", "96", "2", "8", "6", "7", "6", "0", "3", "2"], test_stone_observer.get_current_stones())
        self.assertEqual(test_stone_observer.get_stone_count(), 22)
    
    def test_should_return_correct_stone_count_for_example_input_after_25_blinks(self):
        test_stone_observer = StoneObserver(self.example_input)
        test_stone_observer.blink(25)
        self.assertEqual(55312, test_stone_observer.get_stone_count())

class TestMultiThreadedStoneObserver(unittest.TestCase):
    example_input = """125 17"""
    
    def test_parses_input_into_a_set_of_stone_observers(self):
        test_super_stone_observer = MultiThreadedStoneObserver(self.example_input)
        self.assertEqual(len(test_super_stone_observer.stones_tree_observers), 2)
        self.assertListEqual(["125"], test_super_stone_observer.stones_tree_observers[0].get_current_stones())
        self.assertListEqual(["17"], test_super_stone_observer.stones_tree_observers[1].get_current_stones())
    
    def test_running_in_parallel_returns_same_result(self):
        test_super_stone_observer = MultiThreadedStoneObserver(self.example_input)
        self.assertEqual(55312, test_super_stone_observer.run_obsevers_in_parallel(25))

class TestDictionaryStoneObserver(unittest.TestCase):
    example_input = """125 17"""
    
    def test_parses_input_to_dictionary(self):
        test_dict_stone_observer = DictionaryStoneObserver(self.example_input)
        self.assertDictEqual({
            "125": 1,
            "17": 1
        }, test_dict_stone_observer.stones)

if __name__ == "__main__":
    unittest.main()