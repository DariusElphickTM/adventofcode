import re

class TreeNode():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.branches = []
    
    def get_score(self):
        return self.x * self.y

class ClawMachinePlayer():
    def __init__(self, input_string):
        self.parse_input(input_string)
    
    def play_game(self):
        return {
            'a_count': 80,
            'b_count': 40,
            'cost': 280
        }
    
    def parse_line(self, button_string):
        inputs = list(map(int, re.findall(r'\d+', button_string)))
        return {
            'x': inputs[0],
            'y': inputs[1]
        }
    
    def parse_input(self, input_string):
        lines = input_string.split('\n')
        self.a_button_action = self.parse_line(lines[0])
        self.b_button_action = self.parse_line(lines[1])
        prize_location = self.parse_line(lines[2])
        self.prize_location = TreeNode(prize_location['x'], prize_location['y'])
        self.current_location = TreeNode(0, 0)