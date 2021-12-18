import math
from typing import List
from typing import Union


def add_snailfish_list(
    snailfish_list: List[List[Union[int, str]]]
) -> int:
    snailfish_result = snailfish_list[0]
    for snailfish in snailfish_list[1:]:
        snailfish_result = add_snailfish_pair(snailfish_result, snailfish)
    magnitude = compute_magnitude(snailfish_result)
    return magnitude


def add_snailfish_pair(
    snailfish1: List[Union[int, str]],
    snailfish2: List[Union[int, str]],
) -> List[Union[int, str]]:
    snailfish_result = ["[", *snailfish1, *snailfish2, "]"]
    reduction = True
    while reduction:
        reduction = False
        nested = True
        while nested:
            nested = False
            brackets_counter = 0
            for i, letter in enumerate(snailfish_result):
                if isinstance(letter, int) and brackets_counter > 4:
                    snailfish_result = explode(snailfish_result, i)
                    nested = True
                    reduction = True
                    break
                elif letter == "[":
                    brackets_counter += 1
                elif letter == "]":
                    brackets_counter -= 1
        for i, letter in enumerate(snailfish_result):
            if isinstance(letter, int) and letter >= 10:
                snailfish_result = split(snailfish_result, i)
                reduction = True
                break
    return snailfish_result


def compute_largest_magnitude_pair(
    snailfish_list: List[List[Union[int, str]]]
) -> int:
    largest_magnitude = 0
    for i1 in range(len(snailfish_list)):
        for i2 in range(i1 + 1, len(snailfish_list)):
            magnitude = compute_magnitude(
                add_snailfish_pair(snailfish_list[i1], snailfish_list[i2])
            )
            largest_magnitude = magnitude if magnitude > largest_magnitude else largest_magnitude
            magnitude = compute_magnitude(
                add_snailfish_pair(snailfish_list[i2], snailfish_list[i1])
            )
            largest_magnitude = magnitude if magnitude > largest_magnitude else largest_magnitude
    return largest_magnitude


def compute_magnitude(snailfish_result: List[Union[int, str]]) -> int:
    last_letter = snailfish_result[0]
    i = 1
    magnitude = 0
    while len(snailfish_result) > 1:
        if i >= len(snailfish_result) - 1:
            last_letter = "]"
            i = 1
        letter = snailfish_result[i]
        if isinstance(last_letter, int) and isinstance(letter, int):
            magnitude = last_letter * 3 + letter * 2
            snailfish_result[i - 2] = magnitude
            del snailfish_result[i - 1: i + 2]
            i = i - 2
            letter = snailfish_result[i]
        last_letter = letter
        i += 1
    return magnitude


def explode(snailfish: List[Union[int, str]], index: int) -> List[Union[int, str]]:
    for i in range(max(index - 2, -1), -1, -1):
        if isinstance(snailfish[i], int):
            snailfish[i] += snailfish[index]
            break
    for i in range(min(index + 3, len(snailfish)), len(snailfish)):
        if isinstance(snailfish[i], int):
            snailfish[i] += snailfish[index + 1]
            break
    del snailfish[index - 1 : index + 3]
    snailfish.insert(index - 1, 0)
    return snailfish


def read_from_file(filename: str) -> List[List[Union[int, str]]]:
    with open(filename) as f:
        data_list = [line.rstrip() for line in f]
    snailfish_list = []
    num = ""
    for i, snailfish in enumerate(data_list):
        snailfish_list.append([])
        for letter in snailfish:
            if letter.isnumeric():
                num += letter
            elif num != "":
                snailfish_list[i].append(int(num))
                if letter != ",":
                    snailfish_list[i].append(letter)
                num = ""
            elif letter != ",":
                snailfish_list[i].append(letter)
    return snailfish_list


def split(snailfish: List[Union[int, str]], index: int) -> List[Union[int, str]]:
    num = snailfish[index]
    num1 = math.floor(num / 2)
    num2 = math.ceil(num / 2)
    del snailfish[index]
    snailfish[index : index] = "[", num1, num2, "]"
    return snailfish
