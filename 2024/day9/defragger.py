class Defragger():
    def __init__(self, input_string: str):
        self.disk_map = self.parse_input_string(input_string)
    
    def parse_input_string(self, input_string: str) -> str:
        result = []
        is_file = True
        block_id = 0
        for block_length in input_string:
            block_char = '.'
            if is_file:
                block_char = f'{block_id}'
                block_id += 1
            for i in range(int(block_length)):
                result.append(block_char)
            is_file = not is_file
        return result