class HugeAntenna():
    def __init__(self, antenna_map_string):
        self.antenna_map = self.parse_antenna_map_string(antenna_map_string)
        self.antenna_frequency_list = self.get_all_antenna_frequencies(antenna_map_string)
    
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
        print(antennaA, antennaB, vector)
        print(antinodes)
        return antinodes
    
    def parse_antenna_map_string(self, antenna_map_string):
        return list(map(list, antenna_map_string.split('\n')))
    
    def get_all_antenna_frequencies(self, antenna_map_string):
        unique_characters = list(set(antenna_map_string))
        unique_characters.remove('\n')
        unique_characters.remove('.')
        return unique_characters