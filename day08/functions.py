from typing import Dict
from typing import List
from collections import defaultdict


def count_unique_digits(display: List[List[str]]) -> int:
    count = defaultdict(int)
    for line in display:
        for entry in line[10:]:
            if len(entry) == 2:
                count[0] += 1
            elif len(entry) == 4:
                count[4] += 1
            elif len(entry) == 3:
                count[7] += 1
            elif len(entry) == 7:
                count[8] += 1
    return sum(count.values())


def get_number(map_digits: Dict[str, int], line: List[str]):
    number = 0
    for i in range(4):
        sorted_entry = "".join(sorted(line[14 - i]))
        number += map_digits[sorted_entry] * 10 ** i
    return number


def restore_display(display: List[List[str]]) -> int:
    display_sum = 0
    for line in display:
        digits = defaultdict(set)
        line_digits = defaultdict(lambda: -1)
        map_digits = {}
        for pos, entry in enumerate(line[:10]):
            num = None
            if len(entry) == 2:
                num = 1
            elif len(entry) == 4:
                num = 4
            elif len(entry) == 3:
                num = 7
            elif len(entry) == 7:
                num = 8
            if num is not None:
                line_digits[pos] = num
                sorted_entry = "".join(sorted(entry))
                map_digits[sorted_entry] = num
                digits[num] = {letter for letter in entry}

        for pos, entry in enumerate(line[:10]):
            if line_digits[pos] == -1:
                num = None
                entry_set = {letter for letter in entry}
                if len(entry) == 5:
                    if len(digits[1].intersection(entry_set)) == 2:
                        num = 3
                    elif len(digits[4].intersection(entry_set)) == 3:
                        num = 5
                    elif len(digits[4].intersection(entry_set)) == 2:
                        num = 2
                if num is not None:
                    line_digits[pos] = num
                    sorted_entry = "".join(sorted(entry))
                    map_digits[sorted_entry] = num
                    digits[num] = {letter for letter in entry}

        for pos, entry in enumerate(line[:10]):
            if line_digits[pos] == -1:
                num = None
                entry_set = {letter for letter in entry}
                if len(digits[1].intersection(entry_set)) == 1:
                    num = 6
                elif len(digits[5].union(entry_set)) == 7:
                    num = 0
                elif len(digits[3].intersection(entry_set)) == 5:
                    num = 9
                if num is not None:
                    line_digits[pos] = num
                    sorted_entry = "".join(sorted(entry))
                    map_digits[sorted_entry] = num
                    digits[num] = {letter for letter in entry}

        display_sum += get_number(map_digits, line)
    return display_sum


def read_from_file(filename: str) -> List[List[str]]:
    with open(filename) as f:
        display = [line.rstrip().split(" ") for line in f]
    return display
