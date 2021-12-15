from functions import (
    expand_the_map,
    find_lowest_risk,
    read_from_file,
)


if __name__ == "__main__":
    risk_map = read_from_file("day15")

    print("Solution part 1:")
    print(find_lowest_risk(risk_map))

    print("\nSolution part 2:")
    print(find_lowest_risk(expand_the_map(risk_map, 5)))
