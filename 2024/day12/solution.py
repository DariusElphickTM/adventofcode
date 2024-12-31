from farm_fencing_calculator import FarmFencingCalculator

def main():
    print("Here we go!")
    fencing_calculator = FarmFencingCalculator(read_file("input.txt"))
    
    print("Solution for part 1", fencing_calculator.get_total_cost())
    print("Solution for part 2", fencing_calculator.get_total_discounted_cost())

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()