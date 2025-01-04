from warehouse_watcher import WarehouseWatcher, BigWarehouseWatcher

def main():
    print("Here we go!")
    input_string = read_file("input.txt")
    watcher = WarehouseWatcher(input_string)
    watcher.play_all_moves()
    print("Part 1 result", watcher.get_current_gps_sum())
    
    big_watcher = BigWarehouseWatcher(input_string)
    big_watcher.play_all_moves()
    print("Part 2 result", big_watcher.get_current_gps_sum())

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()