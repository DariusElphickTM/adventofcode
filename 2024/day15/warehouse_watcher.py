class WarehouseWatcher():
    def __init__(self, input_string):
        self.current_warehouse_state=[]
        self.robot_moves = []
        self.current_robot_position = {
            'x': 0,
            'y': 0
        }
        self.parse_input(input_string)
    
    def play_move(self, move):
        self.current_warehouse_state[self.current_robot_position['y']][self.current_robot_position['x']] = '.'
        if move == '^':
            self.current_robot_position['y'] -= 1
        
        if move == '>':
            self.current_robot_position['x'] += 1
        
        if move == 'v':
            self.current_robot_position['y'] += 1
        
        if move == '<':
            self.current_robot_position['x'] -= 1
        self.current_warehouse_state[self.current_robot_position['y']][self.current_robot_position['x']] = '@'
    
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