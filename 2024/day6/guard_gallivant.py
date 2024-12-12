class GuardGallivant():
    def __init__(self, map_string):
        self.parse_map(map_string)
    
    def parse_map(self, map_string):
        rows = map_string.split('\n')
        self.room_map = list(map(list, rows))
        
        for i, row in enumerate(self.room_map):
            for j, column in enumerate(row):
                if(column == '^'):
                    self.guard = {'x': j, 'y': i, 'facing': '^'}
                    self.room_map[i][j] = '.'
                    break
    
    def __str__(self):
        string_representation = self.room_map.copy()
        guard = self.guard
        string_representation[guard['y']][guard['x']] = guard['facing']
        string_representation = list(map("".join, string_representation))
        return "\n".join(string_representation)