import math
from typing import List

import numpy as np


def advanced_align_position_costs(positions: List[int]) -> int:
    min_cost = math.inf
    for horizontal_pos in range(
        math.floor(np.mean(positions)), math.ceil(np.mean(positions)) + 1
    ):
        temp_cost = 0
        for pos in positions:
            gap = abs(pos - horizontal_pos)
            temp_cost += (gap + 1) * gap // 2
        if temp_cost < min_cost:
            min_cost = temp_cost
    return min_cost


def align_position_costs(positions: List[int]) -> int:
    min_cost = math.inf
    for horizontal_pos in range(
        math.floor(np.median(positions)), math.ceil(np.median(positions)) + 1
    ):
        temp_cost = 0
        for pos in positions:
            temp_cost += abs(pos - horizontal_pos)
        if temp_cost < min_cost:
            min_cost = temp_cost
    return min_cost


def read_from_file(filename: str) -> List[int]:
    with open(filename) as f:
        positions = list(map(int, f.readline().rstrip().split(",")))
    return positions
