import re

class TreeNode():
    def __init__(self, x, y, cost_to_get_here, target_score):
        self.x = x
        self.y = y
        self.cost_to_get_here = cost_to_get_here
        self.target_score = target_score
        self.branches = []
    
    def generate_next_steps(self, a_button_action, b_button_action, target):
        self.branches.append(TreeNode(self.x + a_button_action['x'], self.y + a_button_action['y'], self.cost_to_get_here + 3, target.get_score()))
        self.branches.append(TreeNode(self.x + b_button_action['x'], self.y + b_button_action['y'], self.cost_to_get_here + 1, target.get_score()))
    
    def search_for_prize(self, a_button_action, b_button_action, remaining_depth, target, attempt_count):
        print(attempt_count, " ", target.x, target.y, " searching at ", self.x, self.y, " with score ", self.get_score())
        if remaining_depth < 1 or self.x > target.x or self.y > target.y:
            #We've not found the target and we've gone beyond where it will be
            #Assumption that you can't go backwards while playing the game
            return False
        
        result = None
        
        if self.x == target.x and self.y == target.y:
            #Found the target, return the current cost
            result = self.cost_to_get_here
        else:
            #Generate the next steps, sort them by the score, and execute them in order
            self.generate_next_steps(a_button_action, b_button_action, target)
            self.branches.sort(reverse=True)
            for branch in self.branches:
                result = branch.search_for_prize(a_button_action, b_button_action, remaining_depth - 1, target, attempt_count + 1)
                if result:
                    #A branch has returned a cost. Return
                    break
        return result
    
    def __lt__(self, other):
        return self.target_score - self.get_score() < self.target_score - other.get_score()
    
    def get_score(self):
        return self.x * self.y

class ClawMachinePlayer():
    def __init__(self, input_string):
        self.parse_input(input_string)
    
    def play_game(self):
        result = self.current_location.search_for_prize(self.a_button_action, self.b_button_action, 100, self.prize_location, 1)
        print("Result", result)
        return result
    
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
        self.prize_location = TreeNode(prize_location['x'], prize_location['y'], 0, 0)
        self.current_location = TreeNode(0, 0, 0, self.prize_location.get_score())