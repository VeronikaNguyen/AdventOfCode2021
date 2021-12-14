from functions import (
    count_dots_after_first_fold,
    determine_code,
    read_from_file,
)

if __name__ == "__main__":
    paper, fold_instructions = read_from_file("day13")

    print("Solution part 1:")
    print(count_dots_after_first_fold(paper, fold_instructions))

    print("\nSolution part 2:")
    print(determine_code(paper, fold_instructions))
