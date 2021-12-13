from typing import List
from typing import Tuple

import numpy as np


def determine_overlap(thermal_vents: np.ndarray) -> int:
    count_overlap = 0
    for i in range(thermal_vents.shape[0]):
        for j in range(thermal_vents.shape[1]):
            if thermal_vents[i, j] >= 2:
                count_overlap += 1
    return count_overlap


def determine_diagonal_thermal_vents_overlap(
    coordinates: List[List[Tuple[int, int]]], max_x: int, max_y: int
) -> int:
    thermal_vents = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for entry in coordinates:
        if entry[0][0] == entry[1][0]:
            if entry[0][1] < entry[1][1]:
                start_y = entry[0][1]
                end_y = entry[1][1]
            else:
                start_y = entry[1][1]
                end_y = entry[0][1]
            for y in range(start_y, end_y + 1):
                thermal_vents[entry[0][0], y] += 1
        elif entry[0][1] == entry[1][1]:
            if entry[0][0] < entry[1][0]:
                start_x = entry[0][0]
                end_x = entry[1][0]
            else:
                start_x = entry[1][0]
                end_x = entry[0][0]
            for x in range(start_x, end_x + 1):
                thermal_vents[x, entry[0][1]] += 1
        elif abs(entry[0][0] - entry[1][0]) == abs(entry[0][1] - entry[1][1]):
            if entry[0][0] < entry[1][0]:
                x_range = list(range(entry[0][0], entry[1][0] + 1))
            else:
                x_range = list(range(entry[0][0], entry[1][0] - 1, -1))
            if entry[0][1] < entry[1][1]:
                y_range = range(entry[0][1], entry[1][1] + 1)
            else:
                y_range = range(entry[0][1], entry[1][1] - 1, -1)
            for x, y in zip(x_range, y_range):
                thermal_vents[x, y] += 1
    count_overlap = determine_overlap(thermal_vents)
    return count_overlap


def determine_thermal_vents_overlap(
    coordinates: List[List[Tuple[int, int]]], max_x: int, max_y: int
) -> int:
    thermal_vents = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for entry in coordinates:
        if entry[0][0] == entry[1][0]:
            if entry[0][1] < entry[1][1]:
                start_y = entry[0][1]
                end_y = entry[1][1]
            else:
                start_y = entry[1][1]
                end_y = entry[0][1]
            for y in range(start_y, end_y + 1):
                thermal_vents[entry[0][0], y] += 1
        elif entry[0][1] == entry[1][1]:
            if entry[0][0] < entry[1][0]:
                start_x = entry[0][0]
                end_x = entry[1][0]
            else:
                start_x = entry[1][0]
                end_x = entry[0][0]
            for x in range(start_x, end_x + 1):
                thermal_vents[x, entry[0][1]] += 1

    count_overlap = determine_overlap(thermal_vents)
    return count_overlap


def read_from_file(filename: str) -> (List[List[Tuple[int, int]]], int, int):
    with open(filename) as f:
        data = [line.rstrip().split(" -> ") for line in f]

    coordinates = [[] for _ in range(len(data))]
    max_x, max_y = 0, 0

    for i, entry in enumerate(data):
        coordinates[i] = [
            tuple(map(int, entry[0].split(","))),
            tuple(map(int, entry[1].split(","))),
        ]
        if max_x < coordinates[i][0][0]:
            max_x = coordinates[i][0][0]
        elif max_x < coordinates[i][1][0]:
            max_x = coordinates[i][1][0]
        if max_y < coordinates[i][0][1]:
            max_y = coordinates[i][0][1]
        elif max_y < coordinates[i][1][1]:
            max_y = coordinates[i][1][1]
    return coordinates, max_x, max_y
