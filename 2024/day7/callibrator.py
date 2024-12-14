import re

class BridgeCallibrator():
    def __init__(self, callibrations_string):
        self.callibrations = self.parse_callibration_string(callibrations_string)
    
    def get_total_callibration(self, include_third_operator = False):
        result = 0
        for callibration in self.callibrations:
            if self.is_callibration_true(callibration['callibration_result'], callibration['callibration_steps'], include_third_operator):
                result += callibration['callibration_result']
        print("Result", result)
        return result
    
    def is_callibration_true(self, callibration_result, callibration_steps, include_third_operator = False, print_tree = False):
        root = TreeNode('root', callibration_steps[0], 1, callibration_steps, include_third_operator)
        if print_tree:
            self.print_tree(root)
        return self.find_first_instance_of_value_in_tree(root, callibration_result)

    def find_first_instance_of_value_in_tree(self, root, callibration_result):
        if len(root.branches) < 1:
            return root.value == callibration_result
        else:
            results = list(map(lambda branch: self.find_first_instance_of_value_in_tree(branch, callibration_result), root.branches))
            return True in results
    
    def parse_callibration_string(self, callibrations_string):
        callibration_strings = callibrations_string.split('\n')
        callibrations_list = []
        for callibration in callibration_strings:
            index = int(re.search(r'^\d+(?=\:)', callibration).group())
            values = callibration.split(' ')
            values.pop(0)
            callibrations_list.append({'callibration_result': index, 'callibration_steps': list(map(int, values))})
        return callibrations_list
    
    def print_tree(self, root):
        height = self.get_height(root)
        rows = height + 1
        cols = 2 ** (height + 1) - 1
        tree_matrix = [["" for _ in range(cols)] for _ in range(rows)]
        self.inorder(root, 0, (cols - 1) // 2, height, tree_matrix)
        for row in tree_matrix:
            for cell in row:
                if cell == "":
                    print(" ", end="")
                else:
                    print(cell, end="")
            print()
    
    def inorder(self, root, row, col, height, ans):
        if not root:
            return

        # Calculate offset for child positions
        offset = 2 ** (height - row - 1)

        # Traverse the left subtree
        if len(root.branches) > 1:
            self.inorder(root.branches[0], row + 1, col - offset, 
                    height, ans)

        # Place the current node's value in the matrix
        ans[row][col] = str(root)

        # Traverse the right subtree
        if len(root.branches) > 1:
            self.inorder(root.branches[1], row + 1, col + offset, 
                    height, ans)
    
    def get_height(self, root):
        if len(root.branches) < 1:
            return 0
        branch_heights = list(map(self.get_height, root.branches))
        return max(branch_heights) + 1

class TreeNode():
    def __init__(self, operation, current_value, current_index, callibration, include_third_operator):
        self.operation = operation
        self.value = current_value
        self.branches = []
        if current_index < len(callibration):
            next_operation = callibration[current_index]
            next_index = current_index + 1
            self.branches = [
                TreeNode('+', current_value + next_operation, next_index, callibration, include_third_operator),
                TreeNode('*', current_value * next_operation, next_index, callibration, include_third_operator)
            ]
            if include_third_operator:
                self.branches.append(TreeNode('||', int(f'{current_value}{next_operation}'), next_index, callibration, include_third_operator))
    
    def __str__(self):
        return f'{self.operation} {self.value}'.center(6)