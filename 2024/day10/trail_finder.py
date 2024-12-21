class TrailFinder():
    def __init__(self, size = 16):
        self.initialise_trail_map(size)
    
    def initialise_trail_map(self, size):
        self.trail_positions = []
        self.trail_map = [[0] * size for _ in range(size)]
    
    def add_edge(self, x, y, weight):
        self.trail_map[x][y] = weight
        self.trail_map[y][x] = weight
    
    def get_edge(self, x, y):
        return self.trail_map[x][y]
    
    def parse_input(self, input_text):
        self.trail_positions = ['0', '1', '2', '3', '1', '2', '3', '4', '8', '7', '6', '5', '9', '8', '7', '6']
        self.trail_map = [
            [
                0, 1, 0, 0, 
                1, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                -1, 0, 1, 0, 
                0, 1, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, -1, 0, 1, 
                0, 0, 1, 0, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, 0, -1, 0, 
                0, 0, 0, 1, 
                0, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                -1, 0, 0, 0, 
                0, 1, 0, 0, 
                7, 0, 0, 0, 
                0, 0, 0, 0
            ],
            [
                0, -1, 0, 0, 
                -1, 0, 1, 0, 
                0, 5, 0, 0,
                0, 0, 0, 0
            ],
            [
                0, 0, -1, 0, 
                0, -1, 0, 1, 
                0, 0, 3, 0, 
                0, 0, 0, 0
            ],
            [
                0, 0, 0, -1, 
                0, 0, -1, 0, 
                0, 0, 0, 1, 
                0, 0, 0, 0
            ],
            [
                0, 0, 0, 0, 
                -7, 0, 0, 0, 
                0, -1, 0, 0, 
                1, 0, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, -5, 0, 0,
                1, 0, -1, 0, 
                0, 1, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, -1, 0, 
                0, 1, 0, -1, 
                0, 0, 1, 0
            ],
            [
                0, 0, 0, 0,
                0, 0, 0, -1, 
                0, 0, 1, 0, 
                0, 0, 0, 1
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                -1, 0, 0, 0, 
                0, -1, 0, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, -1, 0, 0, 
                1, 0, -1, 0
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, -1, 0, 
                0, 1, 0, -1
            ],
            [
                0, 0, 0, 0, 
                0, 0, 0, 0, 
                0, 0, 0, -1, 
                0, 0, 1, 0
            ]
        ]
    
    def get_trailhead_score(self):
        return 36