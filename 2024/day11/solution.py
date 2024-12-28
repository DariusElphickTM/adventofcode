from stone_observer import StoneObserver, MultiThreadedStoneObserver, DictionaryStoneObserver

def main():
    print("Here we go!")
    """my_stone_observer = StoneObserver(read_file("input.txt"))
    my_stone_observer.blink(25)
    print("Part 1 result", my_stone_observer.get_stone_count())"""
    
    #my_super_stone_observer = MultiThreadedStoneObserver(read_file("input.txt"))
    
    my_super_duper_stone_observer = DictionaryStoneObserver(read_file("input.txt"))
    print("Part 2 result", my_super_duper_stone_observer.observe_stones(75))

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()