import huge_antenna

def main():
    print("Here we go!")
    input_string = read_file("input.txt")
    my_huge_antenna = huge_antenna.HugeAntenna(input_string)
    my_huge_antenna.with_harmonics = True
    print("Part 2 Result", my_huge_antenna.get_antinode_count())

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()