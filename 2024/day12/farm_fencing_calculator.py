import re

class FarmFencingCalculator():
    def __init__(self, input_string):
        self.plots = []
        self.plot_adjacency_matrix = []
        self.row_length = 4
        self.parse_input(input_string)
    
    def calculate_cost_for_region(self, region):
        return region['area'] * region['perimeter']
    
    def calculate_discounted_cost_for_region(self, region):
        return region['area'] * region['sides']
    
    def find_region_via_dfs(self, current_vertex, visited_plots, region_tracker, plant_id):
        #for each plot found
        #mark each visited_plot
        visited_plots[current_vertex]['visited'] = True
        region_tracker[current_vertex]['visited'] = True
        #area += 1
        current_area = 1
        #perimeter = add to perimeter based on adjacency
            #0 adjacency = 4
            #1 adjacency = 3
            #2 adjancency = 2
            #3 adjacency = 1
            #4 adjacency = 0
        current_perimeter = 4
        current_sides = 0
        for i, adjacent_plot in enumerate(self.plot_adjacency_matrix[current_vertex]):
            if adjacent_plot == 1:
                current_perimeter -= 1
                if not visited_plots[i]['visited']:
                    next_plot = self.find_region_via_dfs(i, visited_plots, region_tracker, plant_id)
                    current_area += next_plot['area']
                    current_perimeter += next_plot['perimeter']
                    current_sides += next_plot['sides']
            elif adjacent_plot == 2:
                #This cell is a corner 
                region_tracker[i]['corner'] = True
                current_sides += 1
        
        #need to account for corners at the edges of the map
        
        
        return {
            'plant': plant_id,
            'area': current_area,
            'perimeter': current_perimeter,
            'sides': current_sides
        }
    
    def find_regions(self):
        regions = []
        visited_plots = list(map(lambda plot: {'visited': False}, self.plots))
        for i, plot in enumerate(self.plots):
            if plot == '0':
                #This is a boundary put in to help with detecting corners. Ignore
                continue
            
            #Check if plot already included in a region
            if visited_plots[i]['visited']:
                continue
            #else
            #find every other plot with the same vegetable accessible from this spot
            #set the final area and perimeter on the region
            region_map = list(map(lambda plot: {'visited': False, 'corner':False, 'plot': plot}, self.plots))
            region = self.find_region_via_dfs(i, visited_plots, region_map, plot)
            regions.append(region)
            #Region added. Continue to the next unvisited plot
        return regions
    
    def region_map_plot_character_representation(self, plot):
        if plot['visited']:
            return plot['plot']
        elif plot['corner']:
            return '*'
        else:
            return '0'
    
    def print_region_map(self, region_map):
        print()
        current_map = list(map(self.region_map_plot_character_representation, region_map))
        i = self.row_length
        while i < len(current_map):
            current_map.insert(i, '\n')
            i += self.row_length + 1
        print("".join(current_map))
        print()
    
    def get_total_cost(self, apply_discount = False):
        regions = self.find_regions()
        total = 0
        for region in regions:
            if apply_discount:
                total += self.calculate_discounted_cost_for_region(region)
            else:
                total += self.calculate_cost_for_region(region)
        return total
    
    def get_total_discounted_cost(self):
        return self.get_total_cost(True)
    
    def initialise_farm_map(self, size = 4):
        self.plots = []
        self.plot_adjacency_matrix = [[0] * size for _ in range(size)]
    
    def add_edge(self, x, y, adjacency_matrix, value = 1, bidirectional = True):
        adjacency_matrix[x][y] = value
        if bidirectional:
            adjacency_matrix[y][x] = value
    
    def print_input_grid(self, input_grid):
        print()
        for row in input_grid:
            print(row)
        print()
    
    def pad_row(self, row):
        row_to_list = list(row)
        row_to_list.insert(0, '0')
        row_to_list.append('0')
        return row_to_list
    
    def parse_input(self, input_string):
        input_grid = list(map(self.pad_row, input_string.split('\n')))
        row_length = len(input_grid[0])
        self.row_length = row_length
        input_grid.insert(0, ['0'] * row_length)
        input_grid.append(['0'] * row_length)
        column_height = len(input_grid)
        size = row_length * column_height
        self.initialise_farm_map(size)
        
        current_index = 0
        for i, row in enumerate(input_grid):
            for j, plot in enumerate(row):
                self.plots.append(plot)
                if i > 0: 
                    if input_grid[i - 1][j] == plot:
                        #need to add adjacency above
                        self.add_edge(current_index, current_index - row_length, self.plot_adjacency_matrix)
                
                if i < column_height - 1:
                    if input_grid[i + 1][j] == plot:
                        #need to add adjacency below
                        self.add_edge(current_index, current_index + row_length, self.plot_adjacency_matrix)
                
                if j > 0:
                    if input_grid[i][j - 1] == plot:
                        #need to add adjacency to the left
                        self.add_edge(current_index, current_index - 1, self.plot_adjacency_matrix)
                
                if j < row_length - 1:
                    if input_grid[i][j + 1] == plot:
                        #need to add adjecency to the right
                        self.add_edge(current_index, current_index + 1, self.plot_adjacency_matrix)
                
                if i > 0 and j > 0:
                    #check for a corner in the NW position
                    #concave corner
                    if not input_grid[i - 1][j - 1] == plot and input_grid[i][j - 1] == plot and input_grid[i - 1][j] == plot:
                        self.add_edge(current_index, current_index - row_length - 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex corner
                    if not input_grid[i - 1][j - 1] == plot and not input_grid[i][j - 1] == plot and not input_grid[i - 1][j] == plot:
                        self.add_edge(current_index, current_index - row_length - 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex 2 convex corner
                    if input_grid[i - 1][j - 1] == plot and not input_grid[i][j - 1] == plot and not input_grid[i - 1][j] == plot:
                        self.add_edge(current_index, current_index - row_length - 1, self.plot_adjacency_matrix, 2, False)
                
                if i > 0 and j < row_length - 1:
                    #check for a corner in the NE position
                    #concave corner
                    if not input_grid[i - 1][j + 1] == plot and input_grid[i][j + 1] == plot and input_grid[i - 1][j] == plot:
                        self.add_edge(current_index, current_index - row_length + 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex corner
                    if not input_grid[i - 1][j + 1] == plot and not input_grid[i][j + 1] == plot and not input_grid[i - 1][j] == plot:
                        self.add_edge(current_index, current_index - row_length + 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex 2 convex corner
                    if input_grid[i - 1][j + 1] == plot and not input_grid[i][j + 1] == plot and not input_grid[i - 1][j] == plot:
                        self.add_edge(current_index, current_index - row_length + 1, self.plot_adjacency_matrix, 2, False)
                
                if i < column_height - 1 and j > 0:
                    #check for a corner in the SW position
                    #concave corner
                    if not input_grid[i + 1][j - 1] == plot and input_grid[i][j - 1] == plot and input_grid[i + 1][j] == plot:
                        self.add_edge(current_index, current_index + row_length - 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex corner
                    if not input_grid[i + 1][j - 1] == plot and not input_grid[i][j - 1] == plot and not input_grid[i + 1][j] == plot:
                        self.add_edge(current_index, current_index + row_length - 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex 2 convex corner
                    if input_grid[i + 1][j - 1] == plot and not input_grid[i][j - 1] == plot and not input_grid[i + 1][j] == plot:
                        self.add_edge(current_index, current_index + row_length - 1, self.plot_adjacency_matrix, 2, False)
                
                if i < column_height - 1 and j < row_length - 1:
                    #check for a corner in the SE position
                    #concave corner
                    if not input_grid[i + 1][j + 1] == plot and input_grid[i][j + 1] == plot and input_grid[i + 1][j] == plot:
                        self.add_edge(current_index, current_index + row_length + 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex corner
                    if not input_grid[i + 1][j + 1] == plot and not input_grid[i][j + 1] == plot and not input_grid[i + 1][j] == plot:
                        self.add_edge(current_index, current_index + row_length + 1, self.plot_adjacency_matrix, 2, False)
                    
                    #convex 2 convex corner
                    if input_grid[i + 1][j + 1] == plot and not input_grid[i][j + 1] == plot and not input_grid[i + 1][j] == plot:
                        self.add_edge(current_index, current_index + row_length + 1, self.plot_adjacency_matrix, 2, False)

                current_index += 1