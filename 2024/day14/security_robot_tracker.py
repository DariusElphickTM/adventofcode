import re

class SecurityRobotTracker():
    def __init__(self, input_string, width, height):
        self.room_width = width
        self.room_height = height
        self.robots = self.parse_input(input_string)
    
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
    
    def parse_input(self, input_string):
        return list(map(self.create_robot_from_string, input_string.split('\n')))