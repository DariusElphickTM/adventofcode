from trail_finder import TrailFinder

def main():
    print("Here we go!")
    finder = TrailFinder()
    finder.parse_input(read_file("input.txt"))
    print("Result", finder.get_score_for_all_trailheads())

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()