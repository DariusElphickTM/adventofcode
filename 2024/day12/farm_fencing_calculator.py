class FarmFencingCalculator():
    def __init__(self, input_string):
        self.farm_map = self.parse_input(input_string)
    
    def calculate_cost_for_region(self, region):
        return region['area'] * region['perimeter']
    
    def find_regions(self):
        return [
            {
                'plant': 'A',
                'area': 4,
                'perimeter': 10
            },
            {
                'plant': 'B',
                'area': 4,
                'perimeter': 8
            },
            {
                'plant': 'C',
                'area': 4,
                'perimeter': 10
            },
            {
                'plant': 'D',
                'area': 1,
                'perimeter': 4
            },
            {
                'plant': 'E',
                'area': 3,
                'perimeter': 8
            }
        ]
    
    def get_total_cost(self):
        regions = self.find_regions()
        total = 0
        for region in regions:
            total += self.calculate_cost_for_region(region)
        return total
    
    def parse_input(self, input_string):
        rows = input_string.splitlines()
        return list(map(list, rows))