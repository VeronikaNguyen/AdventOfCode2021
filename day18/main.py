from functions import (
    add_snailfish_list,
    compute_largest_magnitude_pair,
    read_from_file,
)

if __name__ == "__main__":
    snailfish_list = read_from_file("day18")

    print("Solution part 1:")
    print(add_snailfish_list(snailfish_list))

    print("\nSolution part 2:")
    print(compute_largest_magnitude_pair(snailfish_list))
