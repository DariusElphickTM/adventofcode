import copy

class GuardGallivant():
    def __init__(self, map_string):
        self.parse_map(map_string)
        self.step_count = 0
        self.loop_opportunties = 0
    
    def parse_map(self, map_string):
        rows = map_string.split('\n')
        self.room_map = list(map(list, rows))
        
        for i, row in enumerate(self.room_map):
            for j, column in enumerate(row):
                if(column == '^'):
                    self.guard = {'x': j, 'y': i, 'facing': '^'}
                    self.room_map[i][j] = '.'
                    break
    
    def play(self, seek_loop_opportunities = False):
        print("Initial state")
        self.print_state()
        self.step_count = 0
        self.loop_opportunties = 0
        while True:
            next_step = self.take_step(self.guard)
            if next_step['step_count'] > 0:
                self.room_map[self.guard['y']][self.guard['x']] = 'X'
                self.step_count += next_step['step_count']
            self.guard = next_step['next_guard_state']
            if self.guard_out_of_bounds(self.guard):
                print("Finished")
                self.print_state()
                break
            elif seek_loop_opportunities:
                self.loop_opportunties += self.seek_loop_opportunity()
    
    def seek_loop_opportunity(self):
        seeker_guard = self.turn_guard(self.guard)
        turn_count = 0
        loop_opportunity = 0
        while turn_count < 4:
            next_step = self.take_step(seeker_guard)
            self.guard = next_step['next_guard_state']
            self.step_count += next_step['step_count']
            if self.guard_out_of_bounds(self.guard):
                print("No loop found before going out of bounds")
                self.print_state()
                break
        return loop_opportunity
    
    def guard_out_of_bounds(self, guard):
        return guard['y'] < 0 or guard['y'] >= len(self.room_map) or guard['x'] < 0 or guard['x'] >= len(self.room_map[guard['y']])

    def take_step(self, current_guard_position):
        next_guard_position = self.get_guards_next_position(current_guard_position)
        step_count = 0
        if not self.guard_out_of_bounds(next_guard_position):
            if self.room_map[next_guard_position['y']][next_guard_position['x']] == '#':
                next_guard_position = self.turn_guard(current_guard_position)
            else:
                if not self.room_map[next_guard_position['y']][next_guard_position['x']] == 'X':
                    step_count = 1
        else:
            step_count = 1
        return {
            'next_guard_state': next_guard_position,
            'step_count': step_count
        }
    
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