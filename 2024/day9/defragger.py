import copy

class Defragger():
    def __init__(self, input_string: str, whole_file_mode = False):
        self.disk_map = self.parse_input_string(input_string)
        self.disk_block_map = self.parse_input_string_into_block_map(input_string)
        self.whole_file_mode = whole_file_mode
    
    def get_file_system_checksum(self) -> int:
        if self.whole_file_mode:
            return self.get_file_system_checksum_whole_file_mode()
        else:
            return self.get_file_system_checksum_simple_mode()
    
    def get_file_system_checksum_whole_file_mode(self) -> int:
        defragged_disk_map = self.get_defragged_disk_map_whole_file_mode()
        result = 0
        for i, file_block in enumerate(defragged_disk_map):
            if file_block == '.':
                break
            result += i * int(file_block)
        return result
    
    def get_defragged_disk_map_whole_file_mode(self) -> list[str]:
        defragged_disk = copy.deepcopy(self.disk_block_map)
        current_block_pointer = len(defragged_disk) - 1
        while current_block_pointer > 0:
            current_block = defragged_disk[current_block_pointer]
            if current_block['id'] == '.':
                current_block_pointer -= 1
                continue
            seek_size = current_block['size']
            available_free_space = next((i for i, seeking_block in enumerate(defragged_disk) if seeking_block['id'] == '.' and seeking_block['size'] >= seek_size), -1)
            if available_free_space > -1 and available_free_space < current_block_pointer:
                if current_block['size'] == defragged_disk[available_free_space]['size']:
                    #Simple swap
                    defragged_disk[current_block_pointer] = defragged_disk[available_free_space]
                    defragged_disk[available_free_space] = current_block
                else:
                    #Complex swap
                    free_space = defragged_disk[available_free_space]
                    defragged_disk[available_free_space] = current_block
                    defragged_disk[current_block_pointer] = {'id':'.', 'size': current_block['size']}
                    defragged_disk.insert(available_free_space + 1, {'id':'.', 'size': free_space['size'] - current_block['size']})
                    current_block_pointer += 1
            
            self.print_the_block_map(defragged_disk)
            current_block_pointer -= 1
        return defragged_disk
    
    def print_the_block_map(self, block_map):
        print()
        for block in block_map:
            for i in range(block['size']):
                print(block['id'], end = '')
        print()
    
    def get_file_system_checksum_simple_mode(self) -> int:
        defragged_disk_map = self.get_defragged_disk_map_simple_mode()
        result = 0
        for i, file_block in enumerate(defragged_disk_map):
            if file_block == '.':
                break
            result += i * int(file_block)
        return result
    
    def get_defragged_disk_map_simple_mode(self) -> list[str]:
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
    
    def parse_input_string_into_block_map(self, input_string):
        result = []
        is_file = True
        block_id = 0
        for block_length in input_string:
            size = int(block_length)
            if size > 0:
                block_char = '.'
                if is_file:
                    block_char = f'{block_id}'
                    block_id += 1
                result.append({
                    'id': block_char,
                    'size': size
                })
            is_file = not is_file
        return result