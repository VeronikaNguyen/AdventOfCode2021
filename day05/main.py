from functions import (
    determine_diagonal_thermal_vents_overlap,
    determine_thermal_vents_overlap,
    read_from_file,
)

if __name__ == "__main__":
    coordinates, max_x, max_y = read_from_file("day5")

    print("Solution part 1:")
    print(determine_thermal_vents_overlap(coordinates, max_x, max_y))

    print("\nSolution part 2:")
    print(determine_diagonal_thermal_vents_overlap(coordinates, max_x, max_y))
