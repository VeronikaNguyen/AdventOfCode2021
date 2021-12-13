from functions import (
    life_support_rating,
    power_consumption,
    read_from_file,
)


if __name__ == "__main__":
    diagnostic_report = read_from_file("day3")

    print("Solution part 1:")
    print(power_consumption(diagnostic_report))

    print("\nSolution part 2:")
    print(life_support_rating(diagnostic_report))
