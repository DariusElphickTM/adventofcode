import re

class SecurityRobotTracker():
    def __init__(self, input_string, width, height):
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
    
    def track_robots(self, seconds = 1, print_state = False):
        for i in range(seconds):
            self.tick()
            if print_state:
                self.print_current_room_state()
    
    def tick(self):
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
    
    def print_current_room_state(self):
        current_robot_positions = list(map(lambda robot: robot['p'], self.robots))
        room = [[0] * self.room_width for _ in range(self.room_height)]
        for robot_position in current_robot_positions:
            room[robot_position['y']][robot_position['x']] = room[robot_position['y']][robot_position['x']] + 1
        print("Current room state")
        for row in room:
            print(row)
    
    def parse_input(self, input_string):
        return list(map(self.create_robot_from_string, input_string.split('\n')))