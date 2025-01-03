import re
from collections import deque

class TreeNode():
    def __init__(self, x, y, a_count = 0, b_count = 0, current_depth = 0):
        self.x = x
        self.y = y
        self.a_count = a_count
        self.b_count = b_count
        self.current_depth = current_depth
        self.branches = []
    
    def generate_next_steps(self, a_button_action, b_button_action):
        self.branches.append(
            TreeNode(
                self.x + a_button_action['x'], 
                self.y + a_button_action['y'], 
                self.a_count + 1, 
                self.b_count, 
                self.current_depth + 1
            )
        )
        self.branches.append(
            TreeNode(
                self.x + b_button_action['x'], 
                self.y + b_button_action['y'], 
                self.a_count, self.b_count + 1, 
                self.current_depth + 1
            )
        )
    
    def get_path(self):
        return {
            'a_count': self.a_count,
            'b_count': self.b_count
        }
    
    def get_score(self):
        return self.x * self.y
    
    def get_cost(self):
        return self.a_count * 3 + self.b_count

class ComputationalClawMachinePlayer():
    def __init__(self, input_string, id = ''):
        self.id = id
        self.parse_input(input_string)
    
    def search_for_prize_bfs(self, max_button_pushes):
        tried_paths = []
        queue = deque([self.current_location])
        while queue:
            current_node = queue.popleft()
            current_path = current_node.get_path()
            print(self.id, "a", current_path['a_count'], "b", current_path['b_count'], "x", current_node.x, "y", current_node.y)
            
            if current_node.a_count > max_button_pushes or current_node.b_count > max_button_pushes:
                continue
            
            match = None
            for previous_path in tried_paths:
                if (previous_path['a_count'] == current_path['a_count'] and previous_path['b_count'] == current_path['b_count']):
                    match = previous_path
                    break
            
            if not match is None:
                continue
            
            if current_node.x == self.prize_location.x and current_node.y == self.prize_location.y:
                return {
                    'a_count': current_node.a_count,
                    'b_count': current_node.b_count,
                    'cost': current_node.get_cost()
                }
            
            tried_paths.append(current_node.get_path())
            current_node.generate_next_steps(self.a_button_action, self.b_button_action)

            queue.append(current_node.branches[0])
            queue.append(current_node.branches[1])
    
    def play_game(self):
        result = self.search_for_prize_bfs(100)
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
        self.prize_location = TreeNode(prize_location['x'], prize_location['y'])
        self.current_location = TreeNode(0, 0)
        
class MathematicalClawMachinePlayer():
    def __init__(self, input_string, id = '', units_corrected = False):
        self.id = id
        self.parse_input(input_string, units_corrected)
    
    def solve_game_mathematically(self):
        #step 1 - Eliminate B button influence from the linear equation
        step_1_matrix = [
            [
                self.a_vector['x'] * self.b_vector['y'],
                self.a_vector['y'] * self.b_vector['x']
            ], 
            [
                self.b_vector['x'] * self.b_vector['y'],
                self.b_vector['y'] * self.b_vector['x']
            ], 
            [
                self.prize_location['x'] * self.b_vector['y'],
                self.prize_location['y'] * self.b_vector['x']
            ]
        ]
        print("Step 1", step_1_matrix)
        
        #step 2 - Subtract x from y
        step_2_array = [
            step_1_matrix[0][0] - step_1_matrix[0][1],
            step_1_matrix[1][0] - step_1_matrix[1][1],
            step_1_matrix[2][0] - step_1_matrix[2][1]
        ]
        print("Step 2", step_2_array)
        
        #step 3 - find a_count
        a_count = step_2_array[2] / step_2_array[0]
        print("a_count", a_count)
        
        #step 4 - find b_count
        b_count = (self.prize_location['x'] - (self.a_vector['x'] * a_count)) / self.b_vector['x']
        print("b_count", b_count)
        
        #step 5 - if both a_count and b_count are integers, the game is solvable
        if not (a_count.is_integer() and b_count.is_integer()):
            return None
        
        return {
            'a_count': a_count,
            'b_count': b_count,
            'cost': a_count * 3 + b_count
        } 
        
    
    def play_game(self):
        result = self.solve_game_mathematically()
        print("Result", result)
        return result
    
    def parse_line(self, button_string):
        inputs = list(map(int, re.findall(r'\d+', button_string)))
        return {
            'x': inputs[0],
            'y': inputs[1]
        }
    
    def parse_input(self, input_string, units_corrected):
        lines = input_string.split('\n')
        self.a_vector = self.parse_line(lines[0])
        self.b_vector = self.parse_line(lines[1])
        prize_location = self.parse_line(lines[2])
        if units_corrected:
            prize_location = {
                'x': prize_location['x'] + 10000000000000,
                'y': prize_location['y'] + 10000000000000
            }
        self.prize_location = prize_location