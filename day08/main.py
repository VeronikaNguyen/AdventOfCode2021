from functions import (
    count_unique_digits,
    read_from_file,
    restore_display,
)

if __name__ == "__main__":
    display = read_from_file("day8")

    print("Solution part 1:")
    print(count_unique_digits(display))

    print("\nSolution part 2:")
    print(restore_display(display))
