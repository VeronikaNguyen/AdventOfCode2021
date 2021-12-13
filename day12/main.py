from functions import (
    count_paths,
    count_paths_visiting_small_cave_twice,
    read_from_file,
)


if __name__ == "__main__":
    paths = read_from_file("day12")

    print("Solution part 1:")
    print(count_paths(paths))

    print("\nSolution part 2:")
    print(count_paths_visiting_small_cave_twice(paths))