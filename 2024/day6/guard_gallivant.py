import copy

class GuardGallivant():
    def __init__(self, map_string):
        self.parse_map(map_string)
        self.step_count = 0
    
    def parse_map(self, map_string):
        rows = map_string.split('\n')
        self.room_map = list(map(list, rows))
        
        for i, row in enumerate(self.room_map):
            for j, column in enumerate(row):
                if(column == '^'):
                    self.guard = {'x': j, 'y': i, 'facing': '^'}
                    self.room_map[i][j] = '.'
                    break
    
    def play(self):
        print("Initial state")
        self.print_state()
        self.step_count = 0
        while True:
            self.step_count += self.take_step()
            if self.guard_out_of_bounds(self.guard):
                print("Finished")
                self.print_state()
                break
    
    def guard_out_of_bounds(self, guard):
        return guard['y'] < 0 or guard['y'] >= len(self.room_map) or guard['x'] < 0 or guard['x'] >= len(self.room_map[guard['y']])

    def take_step(self):
        next_guard_position = self.get_guards_next_position(self.guard)
        step_count = 0
        if not self.guard_out_of_bounds(next_guard_position):
            if self.room_map[next_guard_position['y']][next_guard_position['x']] == '#':
                self.guard = self.turn_guard(self.guard)
            else:
                self.room_map[self.guard['y']][self.guard['x']] = 'X'
                if not self.room_map[next_guard_position['y']][next_guard_position['x']] == 'X':
                    step_count = 1
                self.guard = next_guard_position
        else:
            self.guard = next_guard_position
            step_count = 1
        return step_count
    
    def get_guards_next_position(self, current_guard_position):
        next_guard_position = current_guard_position.copy()
        if current_guard_position['facing'] == '^':
            next_guard_position['y'] -= 1
        elif current_guard_position['facing'] == '<':
            next_guard_position['x'] -= 1
        elif current_guard_position['facing'] == '>':
            next_guard_position['x'] += 1
        else:
            next_guard_position['y'] += 1
        return next_guard_position
    
    def turn_guard(self, guard):
        next_position = {
            '^': '>',
            '>': 'v',
            'v': '<',
            '<': '^'
        }
        new_guard = guard.copy()
        new_guard['facing'] = next_position[guard['facing']]
        return new_guard
        
    
    def print_state(self):
        print("Step count", self.step_count)
        print(self)
    
    def __str__(self):
        string_representation = copy.deepcopy(self.room_map)
        guard = self.guard
        if not self.guard_out_of_bounds(guard):
            string_representation[guard['y']][guard['x']] = guard['facing']
        string_representation = list(map("".join, string_representation))
        return "\n".join(string_representation)