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
    
    def find_sides_via_dfs(self, current_vertex, visited_plots, adjacency_matrix):
        #for each plot found
        #mark each visited_plot
        visited_plots[current_vertex]['visited'] = True
        for i, adjacent_plot in enumerate(adjacency_matrix[current_vertex]):
            if adjacent_plot == 1:
                if not visited_plots[i]['visited']:
                    self.find_sides_via_dfs(i, visited_plots, adjacency_matrix)
    
    def get_adjacency_matrix_for_sides(self, region_map, region_map_grid):
        size = len(region_map)
        
        adjacency_matrix = [[0] * size for _ in range(size)]
        
        current_index = 0
        for i, row in enumerate(region_map_grid):
            for j, plot in enumerate(row):
                if plot == "S":
                    if i > 0: 
                        if region_map_grid[i - 1][j] == plot:
                            #need to add adjacency above
                            self.add_edge(current_index, current_index - self.row_length, adjacency_matrix)
                    
                    if i < self.row_length - 1:
                        if region_map_grid[i + 1][j] == plot:
                            #need to add adjacency below
                            self.add_edge(current_index, current_index + self.row_length, adjacency_matrix)
                    
                    if j > 0:
                        if region_map_grid[i][j - 1] == plot:
                            #need to add adjacency to the left
                            self.add_edge(current_index, current_index - 1, adjacency_matrix)
                    
                    if j < self.row_length - 1:
                        if region_map_grid[i][j + 1] == plot:
                            #need to add adjecency to the right
                            self.add_edge(current_index, current_index + 1, adjacency_matrix)
                current_index += 1
        return adjacency_matrix
    
    def get_sides_count_from_region_map(self, region_map):
        sides = 0
        clarified_region_map = self.clarify_region_map(region_map)
        visited_plots = list(map(lambda plot: {'visited': False, 'plot': plot}, self.plots))
        region_map_grid = self.get_region_map_grid(region_map)
        adjacency_matrix = self.get_adjacency_matrix_for_sides(region_map, region_map_grid)
        #print(adjacency_matrix)
        for i, plot in enumerate(clarified_region_map):
            #Check it plot not a side, or already accounted for
            if not plot == 'S' or visited_plots[i]['visited']:
                continue
            #else
            #This is a new side we've encountered. Add to the counter.
            sides += 1
            #find every other side accessible from this spot, and mark them as visited
            self.find_sides_via_dfs(i, visited_plots, adjacency_matrix)
            #Side added. Continue to the next unvisited side
        print(sides)
        return sides
    
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
        for i, adjacent_plot in enumerate(self.plot_adjacency_matrix[current_vertex]):
            if adjacent_plot == 1:
                current_perimeter -= 1
                if not visited_plots[i]['visited']:
                    next_plot = self.find_region_via_dfs(i, visited_plots, region_tracker, plant_id)
                    current_area += next_plot['area']
                    current_perimeter += next_plot['perimeter']
            elif adjacent_plot == 2:
                #This cell is next to the current plot. 
                #Let's build a map of the perimeter of the region.
                region_tracker[i]['adjacent'] = True
        
        return {
            'plant': plant_id,
            'area': current_area,
            'perimeter': current_perimeter,
        }
    
    def find_regions(self):
        regions = []
        visited_plots = list(map(lambda plot: {'visited': False}, self.plots))
        for i, plot in enumerate(self.plots):
            #Check if plot already included in a region
            if visited_plots[i]['visited']:
                continue
            #else
            #find every other plot with the same vegetable accessible from this spot
            #set the final area and perimeter on the region
            region_map = list(map(lambda plot: {'visited': False, 'adjacent': False, 'plot': plot}, self.plots))
            region = self.find_region_via_dfs(i, visited_plots, region_map, plot)
            self.print_region_map(region_map)
            region['sides'] = self.get_sides_count_from_region_map(region_map)
            regions.append(region)
            #Region added. Continue to the next unvisited plot
        return regions
    
    def region_map_plot_character_representation(self, plot):
        if plot['visited']:
            return plot['plot']
        elif plot['adjacent']:
            return 'S'
        else:
            return '0'
    
    def clarify_region_map(self, region_map):
        return list(map(self.region_map_plot_character_representation, region_map))
    
    def get_region_map_grid(self, region_map):
        mapped = self.clarify_region_map(region_map)
        result = []
        for i in range(0, len(mapped), self.row_length):
            result.append(mapped[i:i+self.row_length])
        return result
    
    def print_region_map(self, visited_plots):
        print()
        current_map = list(map(self.region_map_plot_character_representation, visited_plots))
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
    
    def add_edge(self, x, y, adjacency_matrix, value = 1):
        adjacency_matrix[x][y] = value
        adjacency_matrix[y][x] = value
    
    def parse_input(self, input_string):
        self.initialise_farm_map(len(re.sub('\n', '', input_string)))
        
        input_grid = list(map(list, input_string.split('\n')))
        column_height = len(input_grid)
        row_length = len(input_grid[0])
        self.row_length = row_length
        
        current_index = 0
        for i, row in enumerate(input_grid):
            for j, plot in enumerate(row):
                self.plots.append(plot)
                if i > 0: 
                    if input_grid[i - 1][j] == plot:
                        #need to add adjacency above
                        self.add_edge(current_index, current_index - row_length, self.plot_adjacency_matrix)
                    else:
                        self.add_edge(current_index, current_index - row_length, self.plot_adjacency_matrix, 2)
                
                if i < column_height - 1:
                    if input_grid[i + 1][j] == plot:
                        #need to add adjacency below
                        self.add_edge(current_index, current_index + row_length, self.plot_adjacency_matrix)
                    else:
                        self.add_edge(current_index, current_index + row_length, self.plot_adjacency_matrix, 2)
                
                if j > 0:
                    if input_grid[i][j - 1] == plot:
                        #need to add adjacency to the left
                        self.add_edge(current_index, current_index - 1, self.plot_adjacency_matrix)
                    else:
                        self.add_edge(current_index, current_index - 1, self.plot_adjacency_matrix, 2)
                
                if j < row_length - 1:
                    if input_grid[i][j + 1] == plot:
                        #need to add adjecency to the right
                        self.add_edge(current_index, current_index + 1, self.plot_adjacency_matrix)
                    else:
                        self.add_edge(current_index, current_index + 1, self.plot_adjacency_matrix, 2)

                current_index += 1
        #self.print_trail_map(self.trail_map)