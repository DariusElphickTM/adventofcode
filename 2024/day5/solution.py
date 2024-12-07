import re
import print_inspector

def main():
    input = read_file("input.txt")
    input_rules = input.split("\n\n", maxsplit=1)[0]
    input_updates = input.split("\n\n")[1]
    
    inspector = print_inspector.PrintInspector(input_rules)
    print("Result", inspector.get_part_1_answer(input_updates))

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()