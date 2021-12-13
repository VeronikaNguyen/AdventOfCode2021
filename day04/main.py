import copy

from functions import (
    determine_first_bingo_score,
    determine_last_bingo_score,
    read_from_file,
)

if __name__ == "__main__":
    print("Solution part 1:")
    random_numbers, bingo_fields = read_from_file("day4")
    print(determine_first_bingo_score(random_numbers, copy.deepcopy(bingo_fields)))

    print("\nSolution part 2:")
    print(determine_last_bingo_score(random_numbers, copy.deepcopy(bingo_fields)))
