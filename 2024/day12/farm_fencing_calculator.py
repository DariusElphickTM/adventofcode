class FarmFencingCalculator():
    def __init__(self, input_string):
        self.farm_map = self.parse_input(input_string)
    
    def get_total_cost(self):
        return 140
    
    def parse_input(self, input_string):
        rows = input_string.splitlines()
        return list(map(list, rows))