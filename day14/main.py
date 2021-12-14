from functions import (
    get_difference_most_least_element,
    read_from_file,
)

if __name__ == "__main__":
    polymer, insertion_rules = read_from_file("day14")

    print("Solution part 1:")
    print(get_difference_most_least_element(polymer, insertion_rules, 10))

    print("\nSolution part 2:")
    print(get_difference_most_least_element(polymer, insertion_rules, 40))
