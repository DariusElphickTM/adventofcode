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
        for move in self.robot_moves:
            self.play_move(move)
    
    def get_current_gps_sum(self):
        current_gps_sum = 0
        for i, row in enumerate(self.current_warehouse_state):
            for j, position in enumerate(row):
                if position == 'O':
                    gps_value = (100 * i) + j
                    current_gps_sum += gps_value
        return current_gps_sum
    
    def print_current_warehouse_state(self):
        print("Current Warehouse state")
        for row in self.current_warehouse_state:
            for position in row:
                print(position, end="")
            print()
        print()
    
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

class BigWarehouseWatcher():
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
        return self.current_warehouse_state[position['y']][position['x']] == '[' or self.current_warehouse_state[position['y']][position['x']] == ']'
    
    def get_all_blocks_affected(self, position):
        blocks = []
        if not self.is_block(position):
            return blocks
        blocks.append(position)
        block_side = self.current_warehouse_state[position['y']][position['x']]
        if block_side == '[':
            blocks.append({
                'y': position['y'],
                'x': position['x'] + 1
            })
        elif block_side == ']':
            blocks.append({
                'y': position['y'],
                'x': position['x'] - 1
            })
        return blocks
    
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
            if move == 'v' or move == '^':
                block_sides = self.get_all_blocks_affected(next_position)
                block_status = list(map(lambda block_side: self.play_move_recursive(move, block_side), block_sides))
                path_clear = False not in block_status
            else:
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
        for move in self.robot_moves:
            self.play_move(move)
    
    def get_current_gps_sum(self):
        current_gps_sum = 0
        for i, row in enumerate(self.current_warehouse_state):
            for j, position in enumerate(row):
                if position == 'O':
                    gps_value = (100 * i) + j
                    current_gps_sum += gps_value
        return current_gps_sum
    
    def print_current_warehouse_state(self):
        print("Current Warehouse state")
        for row in self.current_warehouse_state:
            for position in row:
                print(position, end="")
            print()
        print()
    
    def double_up_row(self, row):
        doubled_up_row = []
        for character in row:
            if character == 'O':
                doubled_up_row.append('[')
                doubled_up_row.append(']')
            elif character == '@': 
                doubled_up_row.append('@')
                doubled_up_row.append('.')
            else:
                doubled_up_row.append(character)
                doubled_up_row.append(character)
        return doubled_up_row
    
    def parse_input(self, input_string):
        input_components = input_string.split('\n\n')
        self.robot_moves = list(input_components[1])
        self.current_warehouse_state = list(map(lambda row: self.double_up_row(list(row)), input_components[0].split('\n')))
        for i, row in enumerate(self.current_warehouse_state):
            for j, position in enumerate(row):
                if position == '@':
                    self.current_robot_position['x'] = j
                    self.current_robot_position['y'] = i
                    return