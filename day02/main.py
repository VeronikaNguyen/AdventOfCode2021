from functions import (
    multiply_depth_position,
    multiply_depth_position_with_aim,
    read_from_file,
)

if __name__ == "__main__":
    commands = read_from_file("day2")

    print("Solution part 1:")
    print(multiply_depth_position(commands))

    print("\nSolution part 2:")
    print(multiply_depth_position_with_aim(commands))
