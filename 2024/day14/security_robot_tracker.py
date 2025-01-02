import re

class SecurityRobotTracker():
    def __init__(self, input_string, width, height):
        self.room_width = width
        self.room_height = height
        self.robots = self.parse_input(input_string)
    
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