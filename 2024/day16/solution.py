from maze_runner import MazeRunner

def main():
    print("Here we go!")
    part_1_runner = MazeRunner(read_file("input.txt"))
    print("Part 1 result", part_1_runner.get_best_path_score())

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == '__main__':
    main()