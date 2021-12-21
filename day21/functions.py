import copy
from typing import List

import numpy as np


def play_game_with_deterministic_dice(positions: List[int]) -> int:
    die_role = 0
    scores = [0, 0]
    idx = 0
    while 1:
        die_role += 1
        if die_role % 3 != 0:
            positions[idx] = (positions[idx] + die_role) % 10
        elif die_role % 3 == 0:
            positions[idx] = (positions[idx] + die_role) % 10
            if positions[idx] == 0:
                scores[idx] += 10
            else:
                scores[idx] += positions[idx]
            idx = (idx + 1) % 2

        if scores[0] >= 1000:
            loosing_idx = 1
            return die_role * scores[loosing_idx]
        elif scores[1] >= 1000:
            loosing_idx = 0
            return die_role * scores[loosing_idx]


def play_game_with_quantum_dice(positions: List[int]) -> int:
    wins = simulate_quantum_dice(positions, [0, 0], [0, 0], 1, 1)
    return wins[0] if wins[0] > wins[1] else wins[1]


def simulate_quantum_dice(
    positions: List[int],
    scores: List[int],
    wins: List[int],
    idx: int,
    possibilities: int,
) -> List[int]:
    three_dice_roles = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }
    if scores[idx] >= 21:
        wins[idx] += possibilities
        return wins
    else:
        idx = (idx + 1) % 2
    for key in three_dice_roles.keys():
        new_possibilities = possibilities * three_dice_roles[key]
        new_positions = copy.deepcopy(positions)
        new_positions[idx] = (positions[idx] + key) % 10
        new_scores = copy.deepcopy(scores)
        if new_positions[idx] == 0:
            new_scores[idx] += 10
        else:
            new_scores[idx] += new_positions[idx]
        wins = simulate_quantum_dice(new_positions, new_scores, wins, idx, new_possibilities)
    return wins


def read_from_file(filename: str) -> List[int]:
    with open(filename) as f:
        data = [line.rstrip().split(" ") for line in f.readlines()]

    positions = [int(data[0][-1]), int(data[1][-1])]
    return positions
