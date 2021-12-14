from collections import defaultdict
import math
from typing import DefaultDict
from typing import Dict


def get_difference_most_least_element(
    polymer: str, insertion_rules: Dict[str, str], steps: int
) -> int:
    pairs_dict = count_pairs(polymer, insertion_rules, steps)
    element_dict = defaultdict(int)
    for key in pairs_dict.keys():
        element_dict[key[0]] += pairs_dict[key]
    element_dict[polymer[-1]] += 1

    min_counter = math.inf
    max_counter = -math.inf
    for value in element_dict.values():
        if value > max_counter:
            max_counter = value
        if value < min_counter:
            min_counter = value
    return max_counter - min_counter


def count_pairs(
    polymer: str,
    insertion_rules: Dict[str, str],
    steps: int,
) -> DefaultDict[str, int]:
    pairs_dict = defaultdict(int)
    for i, letter in enumerate(polymer[:-1]):
        pairs_dict[letter + polymer[i + 1]] += 1
    for _ in range(steps):
        new_pairs_dict = defaultdict(int)
        for key in pairs_dict.keys():
            if pairs_dict[key] > 0:
                inserted_element = insertion_rules[key]
                new_pairs_dict[key[0] + inserted_element] += pairs_dict[key]
                new_pairs_dict[inserted_element + key[1]] += pairs_dict[key]
        pairs_dict = new_pairs_dict
    return pairs_dict


def read_from_file(filename: str) -> (str, Dict[str, str]):
    with open(filename) as f:
        data = [line.rstrip().split(" -> ") for line in f]
    polymer = data[0][0]
    insertion_rules = {}
    for line in data[2:]:
        insertion_rules[line[0]] = line[1]
    return polymer, insertion_rules
