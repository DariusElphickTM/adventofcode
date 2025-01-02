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
    
    def test_it_tracks_the_example_robots_for_100_seconds(self):
        test_tracker = SecurityRobotTracker(
            self.example_input,
            self.example_room_size['width'],
            self.example_room_size['height']
        )
        test_tracker.track_robots(100)
        self.assertListEqual([
            {'p': {'x': 3, 'y': 5}, 'v': {'x': 3, 'y': -3}}, {'p': {'x': 5, 'y': 4}, 'v': {'x': -1, 'y': -3}}, {'p': {'x': 9, 'y': 0}, 'v': {'x': -1, 'y': 2}}, {'p': {'x': 4, 'y': 5}, 'v': {'x': 2, 'y': -1}}, {'p': {'x': 1, 'y': 6}, 'v': {'x': 1, 'y': 3}}, {'p': {'x': 1, 'y': 3}, 'v': {'x': -2, 'y': -2}}, {'p': {'x': 6, 'y': 0}, 'v': {'x': -1, 'y': -3}}, {'p': {'x': 2, 'y': 3}, 'v': {'x': -1, 'y': -2}}, {'p': {'x': 0, 'y': 2}, 'v': {'x': 2, 'y': 3}}, {'p': {'x': 6, 'y': 0}, 'v': {'x': -1, 'y': 2}}, {'p': {'x': 4, 'y': 5}, 'v': {'x': 2, 'y': -3}}, {'p': {'x': 6, 'y': 6}, 'v': {'x': -3, 'y': -3}}
        ], test_tracker.robots)
    
    def test_it_can_track_a_robot_for_several_seconds_with_one_method_call(self):
        test_tracker = SecurityRobotTracker(
            """p=2,4 v=2,-3""",
            self.example_room_size['width'],
            self.example_room_size['height']
        )
        test_tracker.track_robots(5)
        self.assertDictEqual(
            {
                'x': 1,
                'y': 3
            },
            test_tracker.robots[0]['p']
        )
    
    def test_it_should_handle_the_movement_of_one_robot_over_several_seconds(self):
        test_tracker = SecurityRobotTracker(
            """p=2,4 v=2,-3""",
            self.example_room_size['width'],
            self.example_room_size['height']
        )
        self.assertDictEqual(
            {
                'x': 2,
                'y': 4
            },
            test_tracker.robots[0]['p']
        )
        test_tracker.tick()
        self.assertDictEqual(
            {
                'x': 4,
                'y': 1
            },
            test_tracker.robots[0]['p']
        )
        test_tracker.tick()
        self.assertDictEqual(
            {
                'x': 6,
                'y': 5
            },
            test_tracker.robots[0]['p']
        )
        test_tracker.tick()
        self.assertDictEqual(
            {
                'x': 8,
                'y': 2
            },
            test_tracker.robots[0]['p']
        )
        test_tracker.tick()
        self.assertDictEqual(
            {
                'x': 10,
                'y': 6
            },
            test_tracker.robots[0]['p']
        )
        test_tracker.tick()
        self.assertDictEqual(
            {
                'x': 1,
                'y': 3
            },
            test_tracker.robots[0]['p']
        )
    
    def test_it_returns_the_correct_next_position_for_robots_crossing_the_edge(self):
        test_tracker = SecurityRobotTracker(
            """p=0,0 v=-1,-1
p=9,9 v=1,1
p=1,2 v=12,-12""",
            10, 10)
        self.assertDictEqual(
            {
                'x': 9,
                'y': 9
            },
            test_tracker.get_next_position(test_tracker.robots[0])
        )
        self.assertDictEqual(
            {
                'x': 0,
                'y': 0
            },
            test_tracker.get_next_position(test_tracker.robots[1])
        )
        self.assertDictEqual(
            {
                'x': 3,
                'y': 0
            },
            test_tracker.get_next_position(test_tracker.robots[2])
        )
    
    def test_it_returns_the_correct_next_position_for_robots_not_crossing_the_edge(self):
        test_tracker = SecurityRobotTracker(
            """p=0,0 v=1,1
p=10,10 v=-1,-3
p=20,20 v=4,-15
p=30,30 v=-23,22
p=10,10 v=-10,-10
p=2,10 v=-2,0
p=98,98 v=1,1""",
            100, 100)
        self.assertDictEqual(
            {
                'x': 1,
                'y': 1
            },
            test_tracker.get_next_position(test_tracker.robots[0])
        )
        self.assertDictEqual(
            {
                'x': 9,
                'y': 7
            },
            test_tracker.get_next_position(test_tracker.robots[1])
        )
        self.assertDictEqual(
            {
                'x': 24,
                'y': 5
            },
            test_tracker.get_next_position(test_tracker.robots[2])
        )
        self.assertDictEqual(
            {
                'x': 7,
                'y': 52
            },
            test_tracker.get_next_position(test_tracker.robots[3])
        )
        self.assertDictEqual(
            {
                'x': 0,
                'y': 0
            },
            test_tracker.get_next_position(test_tracker.robots[4])
        )
        self.assertDictEqual(
            {
                'x': 0,
                'y': 10
            },
            test_tracker.get_next_position(test_tracker.robots[5])
        )
        self.assertDictEqual(
            {
                'x': 99,
                'y': 99
            },
            test_tracker.get_next_position(test_tracker.robots[6])
        )
        

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