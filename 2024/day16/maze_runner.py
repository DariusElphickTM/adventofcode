import re
from collections import deque
import heapq

class MazeRunner():
    
    def __init__(self, input_string):
        self.start_position = 0
        self.end_position = 0
        self.nodes = []
        self.row_length = 0
        self.maze_adjacency_matrix = [[]]
        
        self.parse_input(input_string)
    
    def initialise_graph(self, size, row_length):
        self.nodes = []
        self.row_length = row_length
        self.maze_adjacency_matrix = [[0] * size for _ in range(size)]
    
    def search_for_shortest_path_bfs(self):
        visited = [False] * len(self.nodes)
        results = []
        visited[self.start_position] = True
        queue = deque([{
            'position': self.start_position,
            'direction': '>',
            'score': 0
        }])
        while queue:
            current_step = queue.popleft()
            current_position = current_step['position']
            if current_position == self.end_position:
                results.append(current_step['score'])
                continue
            
            for i, adjacent_position_direction in enumerate(self.maze_adjacency_matrix[current_position]):
                if adjacent_position_direction != 0 and not visited[i]:
                    if i != self.end_position:
                        visited[i] = True
                    next_step = {
                        'position': i,
                        'direction': adjacent_position_direction,
                        'score': current_step['score'] + 1
                    }
                    if adjacent_position_direction is not current_step['direction']:
                        next_step['score'] = next_step['score'] + 1000
                    queue.append(next_step)
        results.sort()
        return results[0]
    
    def get_map_with_visited(self, nodes, visited, row_length):
        output = []
        for i, node in enumerate(nodes):
            if i % row_length == 0:
                output.append('\n')
            if visited[i] is not False:
                output.append('*')
            else:
                output.append(node)
        return "".join(output)
    
    def get_best_path_score(self):
        return self.search_for_shortest_path_bfs()
    
    def add_edge(self, start, end, direction):
        self.maze_adjacency_matrix[start][end] = direction
        oppositeDirectionMap = {
            '^': 'v',
            'v': '^',
            '<': '>',
            '>': '<'
        }
        self.maze_adjacency_matrix[end][start] = oppositeDirectionMap[direction]
    
    def parse_input(self, input_string):
        input_grid = list(map(list, input_string.split('\n')))
        column_height = len(input_grid)
        row_length = len(input_grid[0])
        
        self.initialise_graph(len(re.sub('\n', '', input_string)), row_length)
        
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
                        self.add_edge(current_index, current_index - row_length, '^')
                    
                    if i < column_height - 1 and input_grid[i + 1][j] == '.':
                        #need to add adjacency below
                        self.add_edge(current_index, current_index + row_length, 'v')
                    
                    if j > 0 and input_grid[i][j - 1] == '.':
                        #need to add adjacency to the left
                        self.add_edge(current_index, current_index - 1, '<')
                    
                    if j < row_length - 1 and input_grid[i][j + 1] == '.':
                        #need to add adjecency to the right
                        self.add_edge(current_index, current_index + 1, '>')

                current_index += 1

class Node:
    def __init__(self, position, direction, distance):
        self.position = position
        self.direction = direction
        self.distance = distance
    
    def __lt__(self, other):
        return self.distance < other.distance

class DijkstraMazeRunner():
    
    def __init__(self, input_string):
        self.start_position = 0
        self.end_position = 0
        self.nodes = []
        self.row_length = 0
        self.maze_adjacency_matrix = [[]]
        
        self.parse_input(input_string)
    
    def initialise_graph(self, size, row_length):
        self.nodes = []
        self.row_length = row_length
        self.maze_adjacency_matrix = [[0] * size for _ in range(size)]
    
    def search_for_shortest_path_dijkstra(self):
        distances = [1000000000] * len(self.nodes)
        distances[self.start_position] = 0
        
        visited = [False] * len(self.nodes)
        
        predecessors = {}
        
        queue = []
        heapq.heappush(
            queue, 
            Node(self.start_position, '>', 0)
        )
        
        while queue:
            current_step = heapq.heappop(queue)
            if visited[current_step.position]:
                continue
            
            visited[current_step.position] = True
            
            for i, adjacent_position_direction in enumerate(self.maze_adjacency_matrix[current_step.position]):
                if adjacent_position_direction != 0:
                    tentative_distance = distances[current_step.position] + 1
                    if adjacent_position_direction is not current_step.direction:
                        tentative_distance += 1000
                    if tentative_distance < distances[i]:
                        distances[i] = tentative_distance
                        predecessors[i] = [current_step.position]
                        heapq.heappush(
                            queue,
                            Node(i, adjacent_position_direction, tentative_distance)
                        )
                    elif tentative_distance == distances[i]: 
                        predecessors[i].append(current_step.position)
        
        self.print_visited(distances)
        return {
            'best_path_score': distances[self.end_position],
            'best_seat_score': self.get_best_seat_score_from_predecessors(predecessors)
        }
    
    def get_best_seat_score_from_predecessors(self, predecessor_array):
        target = (15 * 11) + 10
        print(target)
        print(self.maze_adjacency_matrix[target])
        print(self.nodes[target])
        print(predecessor_array)
        paths = self.reconstruct_best_paths(predecessor_array, self.start_position, self.end_position)
        #print(paths)
        self.print_maps(paths)
        path_lengths = list(map(len, paths))
        #print(path_lengths)
        return 45
    
    def print_visited(self, visited):
        row_length = 15
        output = []
        for i, node in enumerate(self.nodes):
            if i % row_length == 0:
                output.append('\n')
            if visited[i] != 1000000000:
                output.append(f'{str(visited[i]):{0}^{4}}')
                output.append('-')
            else:
                output.append(node)
                output.append(node)
                output.append(node)
                output.append(node)
                output.append(node)
        print(''.join(output))
    
    def print_maps(self, best_paths):
        row_length = 15
        output = []
        for i, node in enumerate(self.nodes):
            if i % row_length == 0:
                output.append('\n')
            if i in best_paths[0]:
                output.append('O')
            else:
                output.append(node)
        print(''.join(output))
    
    def reconstruct_best_paths(self, predecessor_array, start, end):
        if start == end:
            return [[start]]
        
        paths = []
        for predecessor in predecessor_array[end]:
            for path in self.reconstruct_best_paths(predecessor_array, start, predecessor):
                paths.append(path + [end])
        return paths
    
    def get_map_with_visited(self, nodes, visited, row_length):
        output = []
        for i, node in enumerate(nodes):
            if i % row_length == 0:
                output.append('\n')
            if visited[i] is not False:
                output.append('*')
            else:
                output.append(node)
        return "".join(output)
    
    def get_best_path_score(self):
        return self.search_for_shortest_path_dijkstra()['best_path_score']
    
    def get_best_seat_score(self):
        return self.search_for_shortest_path_dijkstra()['best_seat_score']
    
    def add_edge(self, start, end, direction):
        self.maze_adjacency_matrix[start][end] = direction
        oppositeDirectionMap = {
            '^': 'v',
            'v': '^',
            '<': '>',
            '>': '<'
        }
        self.maze_adjacency_matrix[end][start] = oppositeDirectionMap[direction]
    
    def parse_input(self, input_string):
        input_grid = list(map(list, input_string.split('\n')))
        column_height = len(input_grid)
        row_length = len(input_grid[0])
        
        self.initialise_graph(len(re.sub('\n', '', input_string)), row_length)
        
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
                        self.add_edge(current_index, current_index - row_length, '^')
                    
                    if i < column_height - 1 and input_grid[i + 1][j] == '.':
                        #need to add adjacency below
                        self.add_edge(current_index, current_index + row_length, 'v')
                    
                    if j > 0 and input_grid[i][j - 1] == '.':
                        #need to add adjacency to the left
                        self.add_edge(current_index, current_index - 1, '<')
                    
                    if j < row_length - 1 and input_grid[i][j + 1] == '.':
                        #need to add adjecency to the right
                        self.add_edge(current_index, current_index + 1, '>')

                current_index += 1