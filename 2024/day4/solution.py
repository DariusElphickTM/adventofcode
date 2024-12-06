def main():
    print("Let's do wordsearch!")
    parsed_input = parse_input(read_file("input.txt"))
    matches = find_xmas(parsed_input)
    print("Matches", matches)
    
    x_masses = find_x_masses(parsed_input)
    print("X Masses", x_masses)

def parse_input(input: str):
    rows = input.splitlines()
    return list(map(list, rows))

def find_xmas(grid) -> int:
    matches = 0
    for row_index, current_row in enumerate(grid):
        #print(row_index, current_row)
        for column_index, current_column in enumerate(current_row):
            #print(current_column, column_index)
            #Horizontal forward
            if current_column == 'X' and column_index < len(current_row) - 3:
                if grid[row_index][column_index + 1] == 'M':
                    if grid[row_index][column_index + 2] == 'A' and grid[row_index][column_index + 3] == 'S':
                        matches += 1
                
                #Diagonal Down
                if row_index < len(grid) - 3:
                    if grid[row_index + 1][column_index + 1] == 'M':
                        if grid[row_index + 2][column_index + 2] == 'A' and grid[row_index + 3][column_index + 3] == 'S':
                            matches += 1
                
                #Diagonal Up
                if row_index > 2:
                    if grid[row_index - 1][column_index + 1] == 'M':
                        if grid[row_index - 2][column_index + 2] == 'A' and grid[row_index - 3][column_index + 3] == 'S':
                            matches += 1
                
            #Horizontal backward
            if current_column == 'X' and column_index > 2:
                if grid[row_index][column_index - 1] == 'M':
                    if grid[row_index][column_index - 2] == 'A' and grid[row_index][column_index - 3] == 'S':
                        matches += 1
                
                #Diagonal Down
                if row_index < len(grid) - 3:
                    if grid[row_index + 1][column_index - 1] == 'M':
                        if grid[row_index + 2][column_index - 2] == 'A' and grid[row_index + 3][column_index - 3] == 'S':
                            matches += 1
                
                #Diagonal Up
                if row_index > 2:
                    if grid[row_index - 1][column_index - 1] == 'M':
                        if grid[row_index - 2][column_index - 2] == 'A' and grid[row_index - 3][column_index - 3] == 'S':
                            matches += 1
            
            #Vertical down
            if current_column == 'X' and row_index < len(grid) - 3:
                if grid[row_index + 1][column_index] == 'M':
                    if grid[row_index + 2][column_index] == 'A' and grid[row_index + 3][column_index] == 'S':
                        matches += 1
            #Vertical up
            if current_column == 'X' and row_index > 2:
                if grid[row_index - 1][column_index] == 'M':
                    if grid[row_index - 2][column_index] == 'A' and grid[row_index - 3][column_index] == 'S':
                        matches += 1
    return matches

def find_x_masses(grid):
    matches = 0
    for row_index, current_row in enumerate(grid):
        #print(row_index, current_row)
        for column_index, current_column in enumerate(current_row):
            if current_column == 'A' and row_index > 0 and row_index < len(grid) - 1 and column_index > 0 and column_index < len(current_row) - 1:
                #print("Found a valid A", row_index, column_index)
                mas_count = 0
                #forward down
                if grid[row_index - 1][column_index - 1] == 'M' and grid[row_index + 1][column_index + 1] == 'S':
                    mas_count += 1
                
                #forward up
                if grid[row_index + 1][column_index - 1] == 'M' and grid[row_index - 1][column_index + 1] == 'S':
                    mas_count += 1
                
                #backward down
                if grid[row_index - 1][column_index + 1] == 'M' and grid[row_index + 1][column_index - 1] == 'S':
                    mas_count += 1
                
                #backward up
                if grid[row_index + 1][column_index + 1] == 'M' and grid[row_index - 1][column_index - 1] == 'S':
                    mas_count += 1
                
                #print("Mas count", mas_count)
                if(mas_count == 2):
                    matches += 1
    return matches

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()