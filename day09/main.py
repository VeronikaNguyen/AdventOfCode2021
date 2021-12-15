from functions import (
    count_risk_level,
    find_largest_basin,
    read_from_file,
)


if __name__ == "__main__":
    height_map = read_from_file("day9")

    print("Solution part 1:")
    risk_level, sinks = count_risk_level(height_map)
    print(risk_level)

    print("\nSolution part 2:")
    print(find_largest_basin(height_map, sinks))
