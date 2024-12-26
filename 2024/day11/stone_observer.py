class TreeNode():
    def __init__(self, value, branches = []):
        self.value = value
        self.branches = []
        for value in branches:
            self.branches.append(TreeNode(value))

class StoneObserver():
    def __init__(self, input_string):
        self.stones_tree = self.parse_input(input_string)
    
    def blink(self, blink_count):
        print(blink_count)
    
    def get_stone_count(self):
        return len(self.stones_tree.branches)
    
    def get_current_stones(self):
        return self.stones_tree.branches
    
    def parse_input(self, input_string):
        return TreeNode('root', input_string.split(" "))
    
    def tree_to_matrix(self, root, row, col, height, ans):
        if not root:
            return

        # Calculate offset for child positions
        offset = 2 ** (height - row - 1)

        # Traverse the left subtree
        if len(root.branches) > 1:
            self.tree_to_matrix(root.branches[0], row + 1, col - offset, 
                    height, ans)

        # Place the current node's value in the matrix
        ans[row][col] = str(root.value)

        # Traverse the right subtree
        if len(root.branches) > 1:
            self.tree_to_matrix(root.branches[1], row + 1, col + offset, 
                    height, ans)
    
    def print_tree(self, root):
        height = self.get_height(root) 
        rows = height + 1
        cols = 2 ** (height + 1) - 1
        tree_matrix = [["" for _ in range(cols)] for _ in range(rows)]
        self.tree_to_matrix(root, 0, (cols - 1) // 2, height, tree_matrix)
        for row in tree_matrix:
            for cell in row:
                if cell == "":
                    print(" ", end="")
                else:
                    print(cell, end="")
            print()
    
    def get_height(self, root):
        if len(root.branches) < 1:
            return 0
        branch_heights = list(map(self.get_height, root.branches))
        return max(branch_heights) + 1

