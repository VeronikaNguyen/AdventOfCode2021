from functions import (
    distinct_velocities,
    find_highest_y_position,
    find_highest_y_position_fast,
    read_from_file,
)

if __name__ == "__main__":
    x_range, y_range = read_from_file("day17")

    print("Solution part 1:")
    print(find_highest_y_position(x_range, y_range))
    print(find_highest_y_position_fast(y_range))

    print("\nSolution part 2:")
    print(distinct_velocities(x_range, y_range))
