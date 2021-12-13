from typing import List
from typing import Set
from typing import Tuple

import numpy as np


def count_flashes(flash_map: np.ndarray, steps: int) -> int:
    flashes_count = 0
    for _ in range(steps):
        flashes = set()
        for i in range(flash_map.shape[0]):
            for j in range(flash_map.shape[1]):
                flash_map[i, j] += 1
                if flash_map[i, j] == 10:
                    flashes.add((i, j))
                    flashes, flash_map = flash(flashes, flash_map, i, j)
        for f in flashes:
            flash_map[f[0], f[1]] = 0
        flashes_count += len(flashes)
    return flashes_count


def find_adjacent_positions(
    flash_map: np.ndarray, i: int, j: int
) -> List[Tuple[int, int]]:
    adjacent_positions = []
    if i > 0:
        adjacent_positions.append((i - 1, j))
        if j > 0:
            adjacent_positions.append((i - 1, j - 1))
        if j < flash_map.shape[1] - 1:
            adjacent_positions.append((i - 1, j + 1))
    if i < flash_map.shape[0] - 1:
        adjacent_positions.append((i + 1, j))
        if j > 0:
            adjacent_positions.append((i + 1, j - 1))
        if j < flash_map.shape[1] - 1:
            adjacent_positions.append((i + 1, j + 1))

    if j > 0:
        adjacent_positions.append((i, j - 1))
    if j < flash_map.shape[1] - 1:
        adjacent_positions.append((i, j + 1))
    return adjacent_positions


def first_flash(flash_map: np.ndarray) -> int:
    steps = 0
    flashes = set()
    while len(flashes) < (flash_map.shape[0] * flash_map.shape[1]):
        flashes = set()
        for i in range(flash_map.shape[0]):
            for j in range(flash_map.shape[1]):
                flash_map[i, j] += 1
                if flash_map[i, j] == 10:
                    flashes.add((i, j))
                    flashes, flash_map = flash(flashes, flash_map, i, j)
        for f in flashes:
            flash_map[f[0], f[1]] = 0
        steps += 1
    return steps


def flash(
    flashes: Set[Tuple[int, int]], flash_map: np.ndarray, i, j
) -> (Set[Tuple[int, int]], np.ndarray):
    adjacent_positions = find_adjacent_positions(flash_map, i, j)
    for pos in adjacent_positions:
        flash_map[pos] += 1
        if flash_map[pos] == 10:
            flashes.add(pos)
            flashes, flash_map = flash(flashes, flash_map, *pos)
    return flashes, flash_map


def read_from_file(filename: str) -> np.ndarray:
    with open(filename) as f:
        data = [line.rstrip() for line in f]
    flash_map = np.zeros((len(data), len(data[0])), dtype=int)
    for i, line in enumerate(data):
        flash_map[i, :] = list(map(int, list(line)))
    return flash_map
