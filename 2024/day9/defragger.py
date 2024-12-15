import copy

class Defragger():
    def __init__(self, input_string: str):
        self.disk_map = self.parse_input_string(input_string)
    
    def get_file_system_checksum(self) -> int:
        defragged_disk_map = self.get_defragged_disk_map()
        result = 0
        for i, file_block in enumerate(defragged_disk_map):
            if file_block == '.':
                break
            result += i * int(file_block)
        return result
    
    def get_defragged_disk_map(self) -> list[str]:
        defragged_disk = copy.deepcopy(self.disk_map)
        next_free_space_pointer = defragged_disk.index('.')
        next_file_block_pointer = len(defragged_disk) - 1
        while next_free_space_pointer < next_file_block_pointer:
            defragged_disk[next_free_space_pointer] = defragged_disk[next_file_block_pointer]
            defragged_disk[next_file_block_pointer] = '.'
            next_free_space_pointer = defragged_disk.index('.')
            while defragged_disk[next_file_block_pointer] == '.':
                next_file_block_pointer = next_file_block_pointer - 1
        return defragged_disk
    
    def parse_input_string(self, input_string: str) -> list[str]:
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