class HugeAntenna():
    def __init__(self, antenna_map_string):
        self.antenna_map = self.parse_antenna_map_string(antenna_map_string)
        self.antenna_frequency_list = self.get_all_antenna_frequencies(antenna_map_string)
    
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
        antinodes = []
        vector = {
            'x': antennaA['x'] - antennaB['x'], 
            'y': antennaA['y'] - antennaB['y']
        }
        antinodes = [
            {
                'x': antennaA['x'] + vector['x'], 
                'y': antennaA['y'] + vector['y']
            },
            {
                'x': antennaB['x'] - vector['x'], 
                'y': antennaB['y'] - vector['y']
            }
        ]
        return antinodes
    
    def parse_antenna_map_string(self, antenna_map_string):
        return list(map(list, antenna_map_string.split('\n')))
    
    def get_all_antenna_frequencies(self, antenna_map_string):
        unique_characters = list(set(antenna_map_string))
        unique_characters.remove('\n')
        unique_characters.remove('.')
        return unique_characters