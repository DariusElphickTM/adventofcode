from security_robot_tracker import SecurityRobotTracker

def main():
    robot_tracker = SecurityRobotTracker(read_file("input.txt"), 101, 103)
    robot_tracker.track_robots(100)
    print("Part 1 result", robot_tracker.get_safety_factor())
    print("Part 2, searching for tree")
    robot_tracker.track_robots(10000, True)

def read_file(file_name):
    """Reads a text file and returns all of it's contents."""
    with open(file_name, encoding="utf-8") as file:
        file_contents = file.read()
        file.close()
    return file_contents

if __name__ == "__main__":
    main()