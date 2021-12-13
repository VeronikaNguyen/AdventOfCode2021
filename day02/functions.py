from typing import List


def multiply_depth_position(commands: List[List[str]]) -> int:
    depth, position = 0, 0
    for command in commands:
        if command[0] == "forward":
            position += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
    return depth * position


def multiply_depth_position_with_aim(commands: List[List[str]]) -> int:
    aim, depth, position = 0, 0, 0
    for command in commands:
        if command[0] == "forward":
            position += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    return depth * position


def read_from_file(filename: str) -> List[List[str]]:
    with open(filename) as f:
        commands = [line.rstrip().split(" ") for line in f]
    return commands
