from functools import lru_cache
from typing import List


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
    wins1, wins2 = simulate_quantum_dice(0, 0, positions[0], positions[1], 1)
    return wins1 if wins1 > wins2 else wins2


@lru_cache(maxsize=1000000)
def simulate_quantum_dice(
    score1: int, score2: int, position1: int, position2: int, idx: int
) -> (int, int):
    three_dice_roles = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }
    wins1, wins2 = 0, 0
    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1
    for key in three_dice_roles.keys():
        possibilities = three_dice_roles[key]
        if idx == 1:
            new_position1 = (position1 + key) % 10
            new_score1 = score1 + 10 if new_position1 == 0 else score1 + new_position1
            new_wins1, new_wins2 = simulate_quantum_dice(
                new_score1, score2, new_position1, position2, 2
            )
        else:
            new_position2 = (position2 + key) % 10
            new_score2 = score2 + 10 if new_position2 == 0 else score2 + new_position2
            new_wins1, new_wins2 = simulate_quantum_dice(
                score1, new_score2, position1, new_position2, 1
            )
        wins1 += possibilities * new_wins1
        wins2 += possibilities * new_wins2
    return wins1, wins2


def read_from_file(filename: str) -> List[int]:
    with open(filename) as f:
        data = [line.rstrip().split(" ") for line in f.readlines()]

    positions = [int(data[0][-1]), int(data[1][-1])]
    return positions
