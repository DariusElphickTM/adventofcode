import unittest
from security_robot_tracker import SecurityRobotTracker 

class TestSecurityRobotTracker(unittest.TestCase):
    
    example_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
    example_room_size = {
        'width': 11,
        'height': 7
    }

    def test_it_should_parse_input_and_create_a_set_of_robots(self):
        test_tracker = SecurityRobotTracker(self.example_input, self.example_room_size['width'], self.example_room_size['height'])
        self.assertEqual(self.example_room_size['width'], test_tracker.room_width)
        self.assertEqual(self.example_room_size['height'], test_tracker.room_height)
        self.assertListEqual([
            {
                'p': {
                    'x': 0,
                    'y': 4
                },
                'v': {
                    'x': 3,
                    'y': -3
                } 
            },
            {
                'p': {
                    'x': 6,
                    'y': 3
                },
                'v': {
                    'x': -1,
                    'y': -3
                } 
            },
            {
                'p': {
                    'x': 10,
                    'y': 3
                },
                'v': {
                    'x': -1,
                    'y': 2
                } 
            },
            {
                'p': {
                    'x': 2,
                    'y': 0
                },
                'v': {
                    'x': 2,
                    'y': -1
                } 
            },
            {
                'p': {
                    'x': 0,
                    'y': 0
                },
                'v': {
                    'x': 1,
                    'y': 3
                } 
            },
            {
                'p': {
                    'x': 3,
                    'y': 0
                },
                'v': {
                    'x': -2,
                    'y': -2
                } 
            },
            {
                'p': {
                    'x': 7,
                    'y': 6
                },
                'v': {
                    'x': -1,
                    'y': -3
                } 
            },
            {
                'p': {
                    'x': 3,
                    'y': 0
                },
                'v': {
                    'x': -1,
                    'y': -2
                } 
            },
            {
                'p': {
                    'x': 9,
                    'y': 3
                },
                'v': {
                    'x': 2,
                    'y': 3
                } 
            },
            {
                'p': {
                    'x': 7,
                    'y': 3
                },
                'v': {
                    'x': -1,
                    'y': 2
                } 
            },
            {
                'p': {
                    'x': 2,
                    'y': 4
                },
                'v': {
                    'x': 2,
                    'y': -3
                } 
            },
            {
                'p': {
                    'x': 9,
                    'y': 5
                },
                'v': {
                    'x': -3,
                    'y': -3
                } 
            }
        ], test_tracker.robots)

if __name__ == "__main__":
    unittest.main()