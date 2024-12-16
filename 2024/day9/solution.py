from defragger import Defragger

def main():
    print("Here we go!")
    input_string = read_file("input.txt")
    defragger = Defragger(input_string, True)
    print("Part 2 Result", defragger.get_file_system_checksum())

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()