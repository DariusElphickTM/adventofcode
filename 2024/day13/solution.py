from claw_machine_player import ClawMachinePlayer

def play_game_and_return_result(input_string):
    player = ClawMachinePlayer(input_string)
    return player.play_game()

def main():
    print("Here we go!")
    
    input_string = read_file("input.txt")
    input_strings = input_string.split('\n\n')
    results = list(map(play_game_and_return_result, input_strings))
    print(results)

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()