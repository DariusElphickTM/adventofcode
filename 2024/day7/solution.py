import callibrator

def main():
    print("Here we go!")
    input_string = read_file("input.txt")
    my_callibrator = callibrator.BridgeCallibrator(input_string)
    my_callibrator.get_total_callibration(True)

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()