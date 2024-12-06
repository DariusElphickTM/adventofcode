def main():
    print("Hello World")

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
            #Horizontal backward
            if current_column == 'X' and column_index > 2:
                if grid[row_index][column_index - 1] == 'M':
                    if grid[row_index][column_index - 2] == 'A' and grid[row_index][column_index - 3] == 'S':
                        matches += 1
            #Vertical down
            if current_column == 'X' and row_index < len(grid) - 3:
                if grid[row_index + 1][column_index] == 'M':
                    if grid[row_index + 2][column_index] == 'A' and grid[row_index + 3][column_index] == 'S':
                        matches += 1
    return matches

if __name__ == "__main__":
    main()