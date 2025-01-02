import re

class SecurityRobotTracker():
    def __init__(self, input_string, width, height):
        self.seconds_elapsed = 0
        self.room_width = width
        self.room_height = height
        self.robots = self.parse_input(input_string)
    
    def get_safety_factor(self):
        quadrant_counts = self.get_quadrant_counts()
        return quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]
    
    def get_quadrant_counts(self):
        current_robot_positions = self.get_current_robot_positons()
        first_quadrant = list(filter(
            lambda robot: robot['x'] < (self.room_width / 2) - 1 and robot['y'] < (self.room_height / 2) - 1, 
            current_robot_positions
        ))
        second_quadrant = list(filter(
            lambda robot: robot['x'] > self.room_width / 2 and robot['y'] < (self.room_height / 2) - 1, 
            current_robot_positions
        ))
        third_quadrant = list(filter(
            lambda robot: robot['x'] < (self.room_width / 2) - 1 and robot['y'] > self.room_height / 2, 
            current_robot_positions
        ))
        fourth_quadrant = list(filter(
            lambda robot: robot['x'] > self.room_width / 2 and robot['y'] > self.room_height / 2, 
            current_robot_positions
        ))
        return [
            len(first_quadrant), 
            len(second_quadrant), 
            len(third_quadrant), 
            len(fourth_quadrant)
        ]
    
    def get_robots_in_top_half(self):
        current_robot_positions = self.get_current_robot_positons()
        return list(filter(
            lambda robot: robot['y'] < (self.room_height / 2) - 1, 
            current_robot_positions
        ))
    
    def check_for_christmas_tree(self):
        #Assumption that the tree fills the room. This may not be the case. For all I know it's a tiny tree.
        test_set = self.create_floor_grid(self.get_robots_in_top_half(), self.room_width, int(self.room_height / 2))
        for i, row in enumerate(test_set):
            for j, column in enumerate(test_set):
                #Assumption that I can look for a triangle to identify the top of the tree
                if (i > len(test_set) - 6) or j < 5 or j > len(test_set[0]) - 6:
                    continue
                
                if not test_set[i][j] == 0:
                    if (not test_set[i+1][j-1] == 0) and (not test_set[i+2][j-2] == 0) and (not test_set[i+3][j-3] == 0) and (not test_set[i+4][j-4] == 0) and (not test_set[i+5][j-5] == 0) and (not test_set[i+1][j+1] == 0) and (not test_set[i+2][j+2] == 0) and (not test_set[i+3][j+3] == 0) and (not test_set[i+4][j+4] == 0) and (not test_set[i+5][j+5] == 0):
                        print("Triangle detected")
                        self.print_current_room_state()
                        return True
        return False
    
    def track_robots(self, seconds = 1, check_for_christmas_tree=False, print_state=False):
        self.seconds_elapsed = 0
        for i in range(seconds):
            self.tick()
            if check_for_christmas_tree:
                result = self.check_for_christmas_tree()
                if result:
                    print(f'Christmas tree detected after {self.seconds_elapsed} seconds')
                    break
            if print_state:
                self.print_current_room_state()
    
    def tick(self):
        self.seconds_elapsed += 1
        for robot in self.robots:
            robot['p'] = self.get_next_position(robot)
    
    def get_next_position(self, robot):
        current_position = robot['p']
        vector = robot['v']
        next_position = {
            'x': current_position['x'] + vector['x'],
            'y': current_position['y'] + vector['y']
        }
        
        if next_position['x'] < 0:
            next_position['x'] = next_position['x'] + self.room_width
        elif next_position['x'] >= self.room_width:
            next_position['x'] = next_position['x'] - self.room_width
        
        if next_position['y'] < 0:
            next_position['y'] = next_position['y'] + self.room_height
        elif next_position['y'] >= self.room_height:
            next_position['y'] = next_position['y'] - self.room_height
        
        return next_position
    
    def create_robot_from_string(self, robot_string):
        robot_properties = re.findall(r'\-*\d+', robot_string)
        return {
            'p': {
                'x': int(robot_properties[0]),
                'y': int(robot_properties[1])
            },
            'v': {
                'x': int(robot_properties[2]),
                'y': int(robot_properties[3])
            } 
        }
    
    def get_current_robot_positons(self):
        return list(map(lambda robot: robot['p'], self.robots))
    
    def create_floor_grid(self, robot_positons, width, height):
        room = [[0] * width for _ in range(height)]
        for robot_position in robot_positons:
            room[robot_position['y']][robot_position['x']] = room[robot_position['y']][robot_position['x']] + 1
        return room
    
    def print_current_room_state(self, room_override=None):
        if not room_override is None:
            room = room_override
        else:
            current_robot_positions = list(map(lambda robot: robot['p'], self.robots))
            room = self.create_floor_grid(current_robot_positions, self.room_width, self.room_height)
        print("Current room state")
        for row in room:
            for position in row:
                print(position, end="")
            print()
    
    def parse_input(self, input_string):
        return list(map(self.create_robot_from_string, input_string.split('\n')))