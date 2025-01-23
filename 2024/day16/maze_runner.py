import re
from collections import deque

class MazeRunner():
    def __init__(self, input_string):
        self.start_position = 0
        self.end_position = 0
        self.nodes = []
        self.maze_adjacency_matrix = [[]]
        
        self.parse_input(input_string)
    
    def initialise_graph(self, size):
        self.nodes = []
        self.maze_adjacency_matrix = [[0] * size for _ in range(size)]
    
    def search_for_shortest_path_bfs(self, nodes, adjacency_matrix, start_position, end_position):
        visited = [False] * len(nodes)
        visited[start_position] = True
        queue = deque([start_position])
        print("Starting at", start_position)
        while queue:
            current_position = queue.popleft()
            print(current_position)
            if current_position == end_position:
                print("Found the end at position", current_position)
            
            for i, adjacent_position in enumerate(adjacency_matrix[current_position]):
                if adjacent_position == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
        print("Here's the nodes we visited", visited)
    
    def get_best_path(self):
        return """###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############"""
    
    def get_best_path_score(self):
        self.search_for_shortest_path_bfs(self.nodes, self.maze_adjacency_matrix, self.start_position, self.end_position)
        return 7036
    
    def add_edge(self, start, end, weight = 1):
        self.maze_adjacency_matrix[start][end] = weight
        self.maze_adjacency_matrix[end][start] = weight
    
    def parse_input(self, input_string):
        input_grid = list(map(list, input_string.split('\n')))
        column_height = len(input_grid)
        row_length = len(input_grid[0])
        
        self.initialise_graph(len(re.sub('\n', '', input_string)))
        
        current_index = 0
        for i, row in enumerate(input_grid):
            for j, position in enumerate(row):
                self.nodes.append(position)
                
                #Walls have no adjacencies
                if not position == '#':
                    if position == 'S':
                        self.start_position = len(self.nodes) - 1
                    elif position == 'E':
                        self.end_position = len(self.nodes) - 1
                    
                    if i > 0 and input_grid[i - 1][j] == '.':
                        #need to add adjacency above
                        self.add_edge(current_index, current_index - row_length)
                    
                    if i < column_height - 1 and input_grid[i + 1][j] == '.':
                        #need to add adjacency below
                        self.add_edge(current_index, current_index + row_length)
                    
                    if j > 0 and input_grid[i][j - 1] == '.':
                        #need to add adjacency to the left
                        self.add_edge(current_index, current_index - 1)
                    
                    if j < row_length - 1 and input_grid[i][j + 1] == '.':
                        #need to add adjecency to the right
                        self.add_edge(current_index, current_index + 1)

                current_index += 1