import guard_gallivant

def main():
    print("Here we go!")
    input_string = read_file("input.txt")
    gallivanter = guard_gallivant.GuardGallivant(input_string)
    gallivanter.fuck_it_time_to_brute_force()
    print("Loop opportunity count", gallivanter.loop_opportunties)

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()