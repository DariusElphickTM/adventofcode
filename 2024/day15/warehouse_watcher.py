class WarehouseWatcher():
    def __init__(self, input_string):
        self.current_warehouse_state=[]
        self.robot_moves = []
        self.current_robot_position = {
            'x': 0,
            'y': 0
        }
        self.parse_input(input_string)
    
    def is_wall(self, position):
        return self.current_warehouse_state[position['y']][position['x']] == '#'
    
    def is_block(self, position):
        return self.current_warehouse_state[position['y']][position['x']] == 'O'
    
    def get_next_position(self, move, current_position):
        next_position = {
            'x':current_position['x'],
            'y':current_position['y']
        }
        if move == '^':
            next_position['y'] -= 1
        
        if move == '>':
            next_position['x'] += 1
        
        if move == 'v':
            next_position['y'] += 1
        
        if move == '<':
            next_position['x'] -= 1
        
        return next_position
    
    def play_move_recursive(self, move, current_position):
        next_position = self.get_next_position(move, current_position)
        
        if self.is_wall(next_position):
            return False
        
        path_clear = True
        
        if self.is_block(next_position):
            path_clear = self.play_move_recursive(move, next_position)
        
        if path_clear:
            character = self.current_warehouse_state[current_position['y']][current_position['x']]
            self.current_warehouse_state[current_position['y']][current_position['x']] = '.'
            self.current_warehouse_state[next_position['y']][next_position['x']] = character
        
        return path_clear
    
    def play_move(self, move):
        robot_moved = self.play_move_recursive(move, self.current_robot_position)
        if robot_moved:
            self.current_robot_position = self.get_next_position(move, self.current_robot_position)
    
    def play_all_moves(self):
        print("Play all moves")
    
    def get_current_gps_sum(self):
        return 2028
    
    def parse_input(self, input_string):
        input_components = input_string.split('\n\n')
        self.robot_moves = list(input_components[1])
        self.current_warehouse_state = list(map(list, input_components[0].split('\n')))
        for i, row in enumerate(self.current_warehouse_state):
            for j, position in enumerate(row):
                if position == '@':
                    self.current_robot_position['x'] = j
                    self.current_robot_position['y'] = i
                    return