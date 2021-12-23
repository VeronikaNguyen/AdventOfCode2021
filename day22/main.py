import math

from functions import (
    count_lit_cubes_inside_region,
    read_from_file,
)


if __name__ == "__main__":
    instructions = read_from_file("day22")

    print("Solution part 1:")
    forbidden_intervals = [
        [[51, math.inf], [-math.inf, math.inf], [-math.inf, math.inf]],
        [[-math.inf, math.inf], [51, math.inf], [-math.inf, math.inf]],
        [[-math.inf, math.inf], [-math.inf, math.inf], [51, math.inf]],
        [[-math.inf, -51], [-math.inf, math.inf], [-math.inf, math.inf]],
        [[-math.inf, math.inf], [-math.inf, -51], [-math.inf, math.inf]],
        [[-math.inf, math.inf], [-math.inf, math.inf], [-math.inf, -51]],
    ]

    print(count_lit_cubes_inside_region(instructions, forbidden_intervals))

    print("\nSolution part 2:")
    print(count_lit_cubes_inside_region(instructions, []))
