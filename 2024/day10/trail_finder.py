import re

class TrailFinder():
    def __init__(self, size = 16):
        self.initialise_trail_map(size)
    
    def initialise_trail_map(self, size):
        self.trail_positions = []
        self.trail_map = [[0] * size for _ in range(size)]
    
    def add_edge(self, x, y, weight):
        self.trail_map[x][y] = weight
    
    def get_edge(self, x, y):
        return self.trail_map[x][y]
    
    def dfs_recurse(self, adjacency_matrix, visited_peaks, current_vertex):
        
        current_trail_score = 0
        
        #print(self.trail_positions[current_vertex], end=" ")
        #self.print_adjacency_matrix(adjacency_matrix[current_vertex])
        
        if self.trail_positions[current_vertex] == '9' and not current_vertex in visited_peaks:
            #print("Reached a 9!")
            current_trail_score += 1
            visited_peaks.append(current_vertex)
        
        for i, weight in enumerate(adjacency_matrix[current_vertex]):
            if weight == 1:
                current_trail_score += self.dfs_recurse(adjacency_matrix, visited_peaks, i)
        return current_trail_score
    
    def perform_depth_first_search(self, starting_vertex):
        visited_peaks = []
        return self.dfs_recurse(self.trail_map, visited_peaks, starting_vertex)
    
    def parse_input(self, input_text):
        self.initialise_trail_map(len(re.sub('\n', '', input_text)))
        
        input_grid = list(map(list, input_text.split('\n')))
        column_height = len(input_grid)
        row_length = len(input_grid[0])
        
        current_index = 0
        for i, row in enumerate(input_grid):
            for j, position in enumerate(row):
                self.trail_positions.append(position)
                if i > 0:
                    #need to add adjacency above
                    above_adjacency = int(input_grid[i - 1][j]) - int(position)
                    self.add_edge(current_index, current_index - row_length, above_adjacency)
                
                if i < column_height - 1:
                    #need to add adjacency below
                    below_adjacency = int(input_grid[i + 1][j]) - int(position)
                    self.add_edge(current_index, current_index + row_length, below_adjacency)
                
                if j > 0:
                    #need to add adjacency to the left
                    left_adjacency = int(input_grid[i][j - 1]) - int(position) 
                    self.add_edge(current_index, current_index - 1, left_adjacency)
                
                if j < row_length - 1:
                    #need to add adjecency to the right
                    right_adjacency = int(input_grid[i][j + 1]) - int(position)
                    self.add_edge(current_index, current_index + 1, right_adjacency)

                current_index += 1
        #self.print_trail_map(self.trail_map)
    
    def print_adjacency_matrix(self, adjacency_matrix):
        current_map = list(map(lambda item: f'{item}, ', adjacency_matrix))
        i = 4
        while i < len(current_map):
            current_map.insert(i, '\n')
            i += 5
        print("".join(current_map))
        print()
    
    def print_trail_map(self, trail_map):
        for row in trail_map:
            self.print_adjacency_matrix(row)
    
    def get_trailhead_score(self, start_vertex):
        return self.perform_depth_first_search(start_vertex)
    
    def get_trailhead_indexes(self):
        trail_head_indexes = []
        for i, postion in enumerate(self.trail_positions):
            if postion == '0':
                trail_head_indexes.append(i)
        return trail_head_indexes
    
    def get_score_for_all_trailheads(self):
        trail_head_indexes = self.get_trailhead_indexes()
        total_score = 0
        for trail_head_index in trail_head_indexes:
            total_score += self.get_trailhead_score(trail_head_index)
        return total_score