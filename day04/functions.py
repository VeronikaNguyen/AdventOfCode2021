from typing import List
from typing import Optional
from typing import Tuple

import numpy as np


def check_for_completion(position: Tuple[int, int], bingo_field: np.ndarray) -> bool:
    row_bingo = True
    column_bingo = True
    for j in range(5):
        if bingo_field[position[0], j] != -1:
            row_bingo = False
            break

    for i in range(5):
        if bingo_field[i, position[1]] != -1:
            column_bingo = False
            break
    return row_bingo or column_bingo


def compute_score(bingo_field: np.ndarray, complete_entry: int):
    res = 0
    for i in range(5):
        for j in range(5):
            if bingo_field[i, j] >= 0:
                res += bingo_field[i, j]
    return res * complete_entry


def find_num_in_bingo_list(
    number: int, bingo_field: np.ndarray
) -> Optional[Tuple[int, int]]:
    for i in range(5):
        for j in range(5):
            if bingo_field[i, j] == number:
                return i, j
    return None


def determine_first_bingo_score(
    random_numbers: List[int], bingo_fields: List[np.ndarray]
) -> int:
    complete, complete_idx, complete_entry = False, 0, 0
    for number in random_numbers:
        for idx in range(len(bingo_fields)):
            position = find_num_in_bingo_list(number, bingo_fields[idx])
            if position is not None:
                complete_entry = bingo_fields[idx][position]
                bingo_fields[idx][position] = -1
                complete = check_for_completion(position, bingo_fields[idx])
                complete_idx = idx
            if complete:
                break
        if complete:
            break
    score = compute_score(bingo_fields[complete_idx], complete_entry)
    return score


def determine_last_bingo_score(
    random_numbers: List[int], bingo_fields: List[np.ndarray]
) -> int:
    complete_keys = set()
    counter = len(bingo_fields)
    complete_idx, complete_entry = 0, 0
    for num in random_numbers:
        for idx in range(len(bingo_fields)):
            if idx not in complete_keys:
                position = find_num_in_bingo_list(num, bingo_fields[idx])
                if position is not None:
                    complete_entry = bingo_fields[idx][position]
                    bingo_fields[idx][position] = -1
                    complete = check_for_completion(position, bingo_fields[idx])
                    complete_idx = idx
                    if complete:
                        complete_keys.add(idx)
                        counter -= 1
                        if counter == 0:
                            break
        if counter == 0:
            break
    score = compute_score(bingo_fields[complete_idx], complete_entry)
    return score


def read_from_file(filename: str) -> (List[int], List[np.ndarray]):
    with open(filename) as f:
        bingo_data = [line.rstrip() for line in f]

    random_numbers = list(map(int, bingo_data[0].split(",")))
    bingo_fields = []
    for i, line in enumerate(bingo_data[1:]):
        if i % 6 == 0:
            bingo_fields.append(np.zeros((5, 5), dtype=int))
        else:
            bingo_fields[i // 6][((i - 1) % 6), :] = list(map(int, line.split()))

    return random_numbers, bingo_fields
