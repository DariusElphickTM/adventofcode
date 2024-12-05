import re
import functools

def main():
    input_text = read_file("input.txt")
    part_two(input_text)

def part_one(input_text):
    valid_commands = re.findall(r'mul\(\d+\,\d+\)', input_text)
    calculations = list(map(execute_command, valid_commands))
    total = functools.reduce(lambda a, b: a + b, calculations)
    return total

def part_two(input_text):
    start_commands = re.findall(r'^.*?(?=don\'t\(\))', input_text)[0]
    do_commands = list(map(str, re.findall(r'(?<=do\(\)).*?(?=don\'t\(\))', input_text)))
    do_commands_totals = list(map(part_one, do_commands))
    total = functools.reduce(lambda a, b: a + b, do_commands_totals) + part_one(start_commands)
    print(total)
    return total

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