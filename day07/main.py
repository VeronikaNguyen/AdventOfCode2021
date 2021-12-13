from functions import (
    advanced_align_position_costs,
    align_position_costs,
    read_from_file,
)

if __name__ == "__main__":
    positions = read_from_file("day7")

    print("Solution part 1:")
    print(align_position_costs(positions))

    print("\nSolution part 2:")
    print(advanced_align_position_costs(positions))
