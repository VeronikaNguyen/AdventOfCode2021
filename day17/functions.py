from typing import List


def determine_in_target_area(
    x_range: List[int], y_range: List[int], x_vel: int, y_vel: int
) -> (bool, int):
    is_in = False
    y_max = 0
    x_pos, y_pos = 0, 0
    while x_pos <= x_range[1] and y_pos >= y_range[0]:
        x_pos += x_vel
        y_pos += y_vel
        x_vel = max(0, x_vel - 1)
        y_vel -= 1
        y_max = max(y_max, y_pos)
        if x_range[0] <= x_pos <= x_range[1] and y_range[0] <= y_pos <= y_range[1]:
            is_in = True
            break
    return is_in, y_max


def distinct_velocities(x_range: List[int], y_range: List[int]) -> int:
    count = 0
    for x_vel in range(x_range[1] + 1):
        for y_vel in range(y_range[0], abs(y_range[0]) * 3, 1):
            is_in, temp_max = determine_in_target_area(x_range, y_range, x_vel, y_vel)
            if is_in:
                count += 1
    return count


def find_highest_y_position(x_range: List[int], y_range: List[int]) -> int:
    y_max = 0
    for x_vel in range(x_range[0] // 2 + 1):
        for y_vel in range(abs(y_range[1]) * 3):
            is_in, temp_max = determine_in_target_area(x_range, y_range, x_vel, y_vel)
            if is_in:
                y_max = max(y_max, temp_max)
    return y_max


def find_highest_y_position_fast(y_range: List[int]) -> int:
    y_max = (y_range[0] + 1) * y_range[0] // 2
    return y_max


def read_from_file(filename: str) -> (List[int], List[int]):
    with open(filename) as f:
        data = f.readline().rstrip().split(" ")

    x_range = list(map(int, data[2][2:].rstrip(",").split("..")))
    y_range = list(map(int, data[3][2:].rstrip(",").split("..")))
    return x_range, y_range
