import unittest
from claw_machine_player import ClawMachinePlayer

class TestClawMachinePlayer(unittest.TestCase):
    example_inputs = [
        {
            'string': """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400""",
            'result': {
                'a_count': 80,
                'b_count': 40,
                'cost': 280
            }
        },
        {
            'string': """Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176""",
            'result': None
        },
        {
            'string': """Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450""",
            'result': {
                'a_count': 38,
                'b_count': 86,
                'cost': 200
            }
        },
        {
            'string': """Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""",
            'result': None
        }
    ]
    
    def test_parses_input_successfully(self):
        test_input = self.example_inputs[0]
        test_player = ClawMachinePlayer(test_input['string'])
        self.assertDictEqual({
            'x': 94,
            'y': 34
        }, test_player.a_button_action)
        self.assertDictEqual({
            'x': 22,
            'y': 67
        }, test_player.b_button_action)
        self.assertDictEqual({
            'x': 8400, 
            'y': 5400
        }, test_player.prize_location)
    
    def test_plays_game_for_first_example(self):
        test_input = self.example_inputs[0]
        test_player = ClawMachinePlayer(test_input['string'])
        self.assertEqual(test_input['result'], test_player.play_game())
    
    def test_plays_game_for_second_example(self):
        test_input = self.example_inputs[1]
        test_player = ClawMachinePlayer(test_input['string'])
        self.assertEqual(test_input['result'], test_player.play_game())
    
    def test_plays_game_for_third_example(self):
        test_input = self.example_inputs[2]
        test_player = ClawMachinePlayer(test_input['string'])
        self.assertEqual(test_input['result'], test_player.play_game())
    
    def test_plays_game_for_fourth_example(self):
        test_input = self.example_inputs[3]
        test_player = ClawMachinePlayer(test_input['string'])
        self.assertEqual(test_input['result'], test_player.play_game())

if __name__ == "__main__":
    unittest.main()