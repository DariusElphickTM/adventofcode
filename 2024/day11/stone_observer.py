class TreeNode():
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

class StoneObserver():
    def __init__(self, input_string):
        self.stones_tree = self.parse_input(input_string)
    
    def blink(self, blink_count):
        print(blink_count)
    
    def get_stone_count(self):
        return len(self.stones_tree.children)
    
    def get_current_stones(self):
        return self.stones_tree.children
    
    def parse_input(self, input_string):
        return TreeNode('root', input_string.split(" "))

