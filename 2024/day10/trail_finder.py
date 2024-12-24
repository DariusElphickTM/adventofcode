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
    
    def dfs_recurse(self, adjacency_matrix, visited, current_vertex):
        visited[current_vertex] = True
        
        print(current_vertex, end=" ")
        
        for i in adjacency_matrix[current_vertex]:
            if i == 1 and not visited[i]:
                self.dfs_recurse(adjacency_matrix, visited, i)
    
    def perform_depth_first_search(self, starting_vertex):
        visited = [False] * len(self.trail_map)
        self.dfs_recurse(self.trail_map, visited, starting_vertex)
    
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
        #self.print_trail_map()
    
    def print_trail_map(self):
        for row in self.trail_map:
            current_map = list(map(lambda item: f'{item}, ', row))
            i = 4
            while i < len(current_map):
                current_map.insert(i, '\n')
                i += 5
            print("".join(current_map))
            print()
    
    def get_trailhead_score(self):
        self.perform_depth_first_search(0)
        return 36