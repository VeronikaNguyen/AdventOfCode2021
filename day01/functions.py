from typing import List


def count_increase_in_measurements(measurements: List[int]) -> int:
    counter = 0
    for i, number in enumerate(measurements[1:]):
        if number > measurements[i]:
            counter += 1
    return counter


def count_three_window_increase_in_measurements(measurements: List[int]) -> int:
    counter = 0
    for i, number in enumerate(measurements[3:]):
        if number > measurements[i]:
            counter += 1
    return counter


def read_from_file(filename: str) -> List[int]:
    with open(filename) as f:
        measurements = [int(line.rstrip()) for line in f]
    return measurements
