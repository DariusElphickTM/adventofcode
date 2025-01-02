from claw_machine_player import MathematicalClawMachinePlayer

def play_game_and_return_result(input_string, id):
    player = MathematicalClawMachinePlayer(input_string, id, True)
    return player.play_game()

def main():
    print("Here we go!")
    
    input_string = read_file("input.txt")
    input_strings = input_string.split('\n\n')
    results = []
    for i, game in enumerate(input_strings):
        results.append(play_game_and_return_result(game, f'{i} of {len(input_strings)}'))
    filtered_results = filter(lambda result: result is not None, results)
    total_cost = 0
    for result in filtered_results:
        total_cost += result['cost']
    print("Part 2 result", total_cost)

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()