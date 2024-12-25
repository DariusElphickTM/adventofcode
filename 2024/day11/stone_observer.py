class StoneObserver():
    def __init__(self, input_string):
        self.current_stones = self.parse_input(input_string)
    
    def get_stone_count(self):
        return len(self.current_stones)
    
    def get_current_stones(self):
        return self.current_stones
    
    def parse_input(self, input_string):
        return input_string.split(" ")
