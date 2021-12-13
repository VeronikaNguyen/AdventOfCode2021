from functions import (
    count_completion_score,
    count_syntax_error_score,
    read_from_file,
)


if __name__ == "__main__":
    brackets = read_from_file("day10")

    print("Solution part 1:")
    error_score, incomplete_brackets = count_syntax_error_score(brackets)
    print(error_score)

    print("\nSolution part 2:")
    print(count_completion_score(incomplete_brackets))
