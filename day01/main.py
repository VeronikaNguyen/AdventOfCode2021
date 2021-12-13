from functions import (
    count_increase_in_measurements,
    count_three_window_increase_in_measurements,
    read_from_file,
)

if __name__ == "__main__":
    measurements = read_from_file("day1")

    print("Solution part 1:")
    print(count_increase_in_measurements(measurements))

    print("\nSolution part 2:")
    print(count_three_window_increase_in_measurements(measurements))
