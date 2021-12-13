import copy

from functions import (
    count_flashes,
    first_flash,
    read_from_file,
)


if __name__ == "__main__":
    flash_map = read_from_file("day11")

    print("Solution part 1:")
    print(count_flashes(copy.deepcopy(flash_map), 100))

    print("\nSolution part 2:")
    print(first_flash(flash_map))
