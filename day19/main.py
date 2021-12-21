from functions import (
    align_scanner,
    determine_largest_manhattan_distance,
    read_from_file,
)


if __name__ == "__main__":
    scanner_list = read_from_file("day19")

    print("Solution part 1:")
    num_beacons, scanner_positions = align_scanner(0, scanner_list)
    print(num_beacons)

    print("\nSolution part 2:")
    print(determine_largest_manhattan_distance(scanner_positions))
