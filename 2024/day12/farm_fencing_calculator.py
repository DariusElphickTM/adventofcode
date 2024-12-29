import re

class FarmFencingCalculator():
    def __init__(self, input_string):
        self.plots = []
        self.plot_adjacency_matrix = []
        self.parse_input(input_string)
    
    def calculate_cost_for_region(self, region):
        return region['area'] * region['perimeter']
    
    def find_regions(self):
        regions = []
        visited_plots = list(map(lambda plot: {'region-identified': False, 'plot': plot}, self.plots))
        for i, plot in enumerate(self.plots):
            #Check if plot already included in a region
            if visited_plots[i]['region-identified']:
                continue
            #else
            #create new region for plot. Assume it's a lone plot
            region = {
                'plant': plot,
                'area': 1,
                'perimeter': 4
            }
            #find every other plot with the same vegetable accessible from this spot
            #for each plot found
                #mark each visited_plot
                #area += 1
                #perimeter = add to perimeter based on adjacency
                    #0 adjacency = 4
                    #1 adjacency = 3
                    #2 adjancency = 2
                    #3 adjacency = 1
                    #4 adjacency = 0
            #set the final area and perimeter on the region
            #add the region to regions
            #continue to the next unvisited plot
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
    
    def initialise_farm_map(self, size = 4):
        self.plots = []
        self.plot_adjacency_matrix = [[0] * size for _ in range(size)]
    
    def add_edge(self, x, y):
        self.plot_adjacency_matrix[x][y] = 1
        self.plot_adjacency_matrix[y][x] = 1
    
    def get_edge(self, x, y):
        return self.plot_adjacency_matrix[x][y]
    
    def parse_input(self, input_string):
        self.initialise_farm_map(len(re.sub('\n', '', input_string)))
        
        input_grid = list(map(list, input_string.split('\n')))
        column_height = len(input_grid)
        row_length = len(input_grid[0])
        
        current_index = 0
        for i, row in enumerate(input_grid):
            for j, plot in enumerate(row):
                self.plots.append(plot)
                if i > 0 and input_grid[i - 1][j] == plot:
                    #need to add adjacency above
                    self.add_edge(current_index, current_index - row_length)
                
                if i < column_height - 1 and input_grid[i + 1][j] == plot:
                    #need to add adjacency below
                    self.add_edge(current_index, current_index + row_length)
                
                if j > 0 and input_grid[i][j - 1] == plot:
                    #need to add adjacency to the left
                    self.add_edge(current_index, current_index - 1)
                
                if j < row_length - 1 and input_grid[i][j + 1] == plot:
                    #need to add adjecency to the right
                    self.add_edge(current_index, current_index + 1)

                current_index += 1
        #self.print_trail_map(self.trail_map)