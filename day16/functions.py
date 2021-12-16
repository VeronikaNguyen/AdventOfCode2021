import re
from typing import List

import numpy as np


def aggregate_values(values: List[int], type_id: int) -> int:
    values = np.array(values)
    if type_id == 0:
        return np.sum(values)
    elif type_id == 1:
        return np.prod(values)
    elif type_id == 2:
        return np.min(values)
    elif type_id == 3:
        return np.max(values)
    elif type_id == 5:
        return 1 if values[0] > values[1] else 0
    elif type_id == 6:
        return 1 if values[0] < values[1] else 0
    elif type_id == 7:
        return 1 if values[0] == values[1] else 0
    else:
        raise ValueError(
            "The variable `type_id` has to be an integer in the range of 0 to 7."
        )


def decode_code(code: str) -> (int, int):
    binary_code = hex_to_binary(code)
    _, version_sum, num = decode_package(binary_code, 0)
    return version_sum, num


def decode_package(binary_code: str, version_sum: int) -> (str, int, int):
    if len(binary_code) <= 3:
        return "", version_sum, 0
    version = int(binary_code[:3], 2)
    type_id = binary_to_int(binary_code[3:6])
    version_sum += version
    if type_id == 4:
        end = 6
        num = ""
        while binary_code[end] == "1":
            num = num + binary_code[end + 1 : end + 5]
            end += 5
        num = int(num + binary_code[end + 1 : end + 5], 2)
        end += 5
    else:
        values = []
        if binary_code[6:7] == "0":
            end = 22
            length_subpackages = int(binary_code[7:22], 2)
            end += length_subpackages
            subpackages_binary_code, version_sum, num = decode_package(
                binary_code[22:end], version_sum
            )
            values.append(num)
            while len(subpackages_binary_code) > 0:
                subpackages_binary_code, version_sum, num = decode_package(
                    subpackages_binary_code, version_sum
                )
                values.append(num)
        else:
            end = 18
            num_subpackages = binary_to_int(binary_code[7:18])
            subpackages_binary_code = binary_code[end:]
            len_before = len(subpackages_binary_code)
            for i in range(num_subpackages):
                subpackages_binary_code, version_sum, num = decode_package(
                    subpackages_binary_code, version_sum
                )
                end += len_before - len(subpackages_binary_code)
                len_before = len(subpackages_binary_code)
                values.append(num)
        num = aggregate_values(values, type_id)
    return binary_code[end:], version_sum, num


def hex_to_binary(code: str) -> str:
    hex_to_binary_dic = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    binary_code = ""
    for letter in code:
        binary_code += hex_to_binary_dic[letter]
    return binary_code


def binary_to_int(binary_code: str) -> int:
    if re.match(binary_code, "^[0]+$"):
        dec_code = 0
    else:
        dec_code = int(binary_code, 2)
    return dec_code


def read_from_file(filename: str) -> str:
    with open(filename) as f:
        code = f.readline().rstrip()
    return code
