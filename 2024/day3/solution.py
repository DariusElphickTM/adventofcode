import re
import functools

def main():
    input_text = read_file("input.txt")
    valid_commands = re.findall(r'mul\(\d+\,\d+\)', input_text)
    calculations = list(map(execute_command, valid_commands))
    total = functools.reduce(lambda a, b: a + b, calculations)
    print(total)

def execute_command(command):
    tuples = list(map(int, re.findall(r'\d+', command)))
    return functools.reduce(lambda a, b: a * b, tuples)

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()