class HugeAntenna():
    def __init__(self, antenna_map_string):
        self.antenna_map = self.parse_antenna_map_string(antenna_map_string)
        self.antenna_frequency_list = self.get_all_antenna_frequencies(antenna_map_string)
        self.with_harmonics = False
    
    def get_antinode_count(self):
        antinodes = []
        for frequency in self.antenna_frequency_list:
            antinodes = antinodes + self.get_antinodes_for_frequency(frequency)
        deduped_antinodes = [dict(t) for t in {tuple(d.items()) for d in antinodes}]
        return len(deduped_antinodes)
    
    def get_antinodes_for_frequency(self, frequency):
        return self.get_antinodes_for_antennae(
            self.get_antennae_matching_frequency(frequency),
            self.get_map_bounds()
        )
    
    def get_map_bounds(self):
        return {'x':len(self.antenna_map[0]), 'y': len(self.antenna_map)}
    
    def get_antennae_matching_frequency(self, frequency):
        antennae = []
        for i, row in enumerate(self.antenna_map):
            for j, column in enumerate(row):
                if self.antenna_map[i][j] == frequency:
                    antennae.append({
                        'x': j,
                        'y': i
                    })
        return antennae
    
    def get_antinodes_for_antennae(self, antennae, bounds):
        antinodes = []
        for i in range(len(antennae) - 1):
            for j in range(i + 1, len(antennae)):
                antinodes = antinodes + self.get_antinodes_within_bounds(antennae[i], antennae[j], bounds)
        return antinodes
    
    def get_antinodes_within_bounds(self, antennaA, antennaB, bounds):
        return list(filter(lambda antinode: antinode['x'] >= 0 and 
            antinode['x'] < bounds['x'] and 
            antinode['y'] >= 0 and 
            antinode['y'] < bounds['y'], self.get_antinodes(antennaA, antennaB)))
    
    def get_antinodes(self, antennaA, antennaB):
        vector = {
            'x': antennaA['x'] - antennaB['x'], 
            'y': antennaA['y'] - antennaB['y']
        }
        inverted_vector = {
            'x': vector['x'] * -1, 
            'y': vector['y'] * -1
        }
        if self.with_harmonics:
            return self.get_antinodes_with_harmonics(antennaA, antennaB, vector)
        else: 
            return [
                self.get_next_position(antennaA, vector),
                self.get_next_position(antennaB, inverted_vector)
            ]
    
    def get_antinodes_with_harmonics(self, antennaA, antennaB, vector):
        inverted_vector = {
            'x': vector['x'] * -1, 
            'y': vector['y'] * -1
        }
        antinodes = []
        current_position = antennaB
        while True:
            next_position = self.get_next_position(current_position, vector)
            if not self.is_out_of_bounds(next_position):
                antinodes.append(next_position)
                current_position = next_position
            else:
                break
        
        current_position = antennaA
        while True:
            next_position = self.get_next_position(current_position, inverted_vector)
            if not self.is_out_of_bounds(next_position):
                antinodes.append(next_position)
                current_position = next_position
            else:
                break
            
        return antinodes
    
    def get_next_position(self, current_position, vector):
        return {
            'x': current_position['x'] + vector['x'], 
            'y': current_position['y'] + vector['y']
        }
    
    def is_out_of_bounds(self, antinode):
        bounds = self.get_map_bounds()
        return antinode['x'] < 0 or antinode['x'] >= bounds['x'] or antinode['y'] < 0 and antinode['y'] >= bounds['y']
    
    def parse_antenna_map_string(self, antenna_map_string):
        return list(map(list, antenna_map_string.split('\n')))
    
    def get_all_antenna_frequencies(self, antenna_map_string):
        unique_characters = list(set(antenna_map_string))
        unique_characters.remove('\n')
        unique_characters.remove('.')
        return unique_characters