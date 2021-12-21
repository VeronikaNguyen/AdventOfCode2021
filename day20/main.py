from functions import (
    count_lit_pixels,
    read_from_file,
)

if __name__ == "__main__":
    enhancement_instructions, image = read_from_file("day20")

    print("Solution part 1:")
    print(count_lit_pixels(enhancement_instructions, image, 2))

    print("\nSolution part 2:")
    print(count_lit_pixels(enhancement_instructions, image, 50))
