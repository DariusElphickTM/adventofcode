def main():
    print("Hello World")

def parse_input(input: str):
    rows = input.splitlines()
    return list(map(list, rows))

if __name__ == "__main__":
    main()