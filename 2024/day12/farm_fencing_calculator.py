class FarmFencingCalculator():
    def __init__(self, input_string):
        self.farm_map = self.parse_input(input_string)
    
    def parse_input(self, input_string):
        rows = input_string.splitlines()
        return list(map(list, rows))