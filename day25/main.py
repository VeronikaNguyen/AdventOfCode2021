from functions import (
    determine_cucumbers_stop,
    read_from_file,
)


if __name__ == "__main__":
    cucumbers = read_from_file("day25")

    print("Solution part 1:")
    print(determine_cucumbers_stop(cucumbers))
