from collections import defaultdict
from typing import Set
from typing import Tuple

import numpy as np


def count_risk_level(height_map: np.ndarray) -> (int, Set[Tuple[int, int]]):
    risk_level = 0
    sinks = set()
    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            if determine_local_minimum(height_map, i, j):
                risk_level += height_map[i, j] + 1
                sinks.add((i, j))
    return risk_level, sinks


def determine_local_minimum(height_map: np.ndarray, i: int, j: int) -> bool:
    if i > 0:
        if height_map[i, j] >= height_map[i - 1, j]:
            return False
    if i < height_map.shape[0] - 1:
        if height_map[i, j] >= height_map[i + 1, j]:
            return False
    if j > 0:
        if height_map[i, j] >= height_map[i, j - 1]:
            return False
    if j < height_map.shape[1] - 1:
        if height_map[i, j] >= height_map[i, j + 1]:
            return False
    return True


def find_largest_basin(height_map: np.ndarray, sinks: set) -> int:
    basin_coordinates = defaultdict(set)
    for i in range(height_map.shape[0]):
        for j in range(height_map.shape[1]):
            if height_map[i, j] != 9 and (i, j) not in sinks:
                pos = (i, j)
                update_coordinates = {pos}
                while pos not in sinks:
                    pos = get_lower_position(height_map, update_coordinates, *pos)
                    update_coordinates.add(pos)
                basin_coordinates[pos].update(update_coordinates)
    basin_size = []
    for key in basin_coordinates:
        basin_size.append(len(basin_coordinates[key]))
    basin_size.sort()
    return basin_size[-1] * basin_size[-2] * basin_size[-3]


def get_lower_position(
    height_map: np.ndarray, update_coordinates, i: int, j: int
) -> (int, int):
    if i > 0:
        if (
            height_map[i, j] >= height_map[i - 1, j]
            and (i - 1, j) not in update_coordinates
        ):
            return i - 1, j
    if i < height_map.shape[0] - 1:
        if (
            height_map[i, j] >= height_map[i + 1, j]
            and (i + 1, j) not in update_coordinates
        ):
            return i + 1, j
    if j > 0:
        if (
            height_map[i, j] >= height_map[i, j - 1]
            and (i, j - 1) not in update_coordinates
        ):
            return i, j - 1
    if j < height_map.shape[1] - 1:
        if (
            height_map[i, j] >= height_map[i, j + 1]
            and (i, j + 1) not in update_coordinates
        ):
            return i, j + 1


def read_from_file(filename: str) -> np.ndarray:
    with open(filename) as f:
        data = [line.rstrip() for line in f]
    height_map = np.zeros((len(data), len(data[0])), dtype=int)
    for i, line in enumerate(data):
        height_map[i, :] = list(map(int, list(line)))
    return height_map
