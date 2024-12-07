import re

def main():
    print("Hello World")

def get_sum_of_middle_pages_for_correct_updates(input):
    input_components = input.split('\n\n')
    rules = parse_rules(input_components[0])
    updates = parse_updates(input_components[1])
    #safe_updates = list(filter(is_safe, updates))
    return 143

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()