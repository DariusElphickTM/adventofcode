import re

class BridgeCallibrator():
    def __init__(self, callibrations_string):
        self.callibrations = self.parse_callibration_string(callibrations_string)
    
    def parse_callibration_string(self, callibrations_string):
        callibration_strings = callibrations_string.split('\n')
        callibrations_dictionary = {}
        for callibration in callibration_strings:
            index = int(re.search(r'^\d+(?=\:)', callibration).group())
            values = callibration.split(' ')
            values.pop(0)
            callibrations_dictionary[index] = list(map(int, values))
        return callibrations_dictionary