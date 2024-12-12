class GuardGallivant():
    def __init__(self, map_string):
        self.parse_map(map_string)
    
    def parse_map(self, map_string):
        rows = map_string.split('\n')
        self.room_map = list(map(list, rows))
        
        for i, row in enumerate(self.room_map):
            for j, column in enumerate(row):
                if(column == '^'):
                    self.guard = {'x': j, 'y': i, 'facing': 'up'}
                    self.room_map[i][j] = '.'
                    break