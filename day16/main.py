from functions import (
    decode_code,
    read_from_file,
)

if __name__ == "__main__":
    code = read_from_file("day16")
    version_sum, num = decode_code(code)

    print("Solution part 1:")
    print(version_sum)

    print("\nSolution part 2:")
    print(num)
