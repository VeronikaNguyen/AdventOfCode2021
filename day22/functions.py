from collections import defaultdict
from typing import List
from typing import Optional
from typing import Union

import numpy as np


def count_lit_cubes_inside_region(
    instructions: List[List[Union[int, List[int]]]],
    forbidden_intervals: List[List[List[Union[int, float]]]],
) -> int:
    lit_intervals = light_cubes_inside_region(instructions, forbidden_intervals)
    lit_cubes = 0
    for interval in lit_intervals:
        lit_cubes += get_volume_of_intervals(interval)
    return lit_cubes


def get_volume(interval: List[List[int]]) -> int:
    volume = 1
    for i in range(3):
        volume *= interval[i][1] - interval[i][0] + 1
    return volume


def get_volume_of_intervals(intervals: List[List[int]]) -> int:
    volume = get_volume(intervals[:3])
    x_nums = {intervals[0][0], intervals[0][1]}
    y_nums = {intervals[1][0], intervals[1][1]}
    z_nums = {intervals[2][0], intervals[2][1]}
    for i in range(3, len(intervals), 3):
        x_nums.add(intervals[i][0])
        x_nums.add(intervals[i][1])
        y_nums.add(intervals[i + 1][0])
        y_nums.add(intervals[i + 1][1])
        z_nums.add(intervals[i + 2][0])
        z_nums.add(intervals[i + 2][1])

    x_intervals = sorted(list(x_nums) + list(x_nums))
    y_intervals = sorted(list(y_nums) + list(y_nums))
    z_intervals = sorted(list(z_nums) + list(z_nums))
    x_idx = defaultdict(list)
    y_idx = defaultdict(list)
    z_idx = defaultdict(list)
    for i, x in enumerate(x_intervals):
        x_idx[x].append(i)
    for i, y in enumerate(y_intervals):
        y_idx[y].append(i)
    for i, z in enumerate(z_intervals):
        z_idx[z].append(i)
    cube = np.ones(
        shape=(len(x_intervals) - 1, len(y_intervals) - 1, len(z_intervals) - 1)
    )
    for i in range(3, len(intervals), 3):
        for x in range(x_idx[intervals[i][0]][0], x_idx[intervals[i][1]][-1]):
            for y in range(
                y_idx[intervals[i + 1][0]][0], y_idx[intervals[i + 1][1]][-1]
            ):
                for z in range(
                    z_idx[intervals[i + 2][0]][0], z_idx[intervals[i + 2][1]][-1]
                ):
                    cube[x, y, z] = 0

    for x in range(cube.shape[0]):
        for y in range(cube.shape[1]):
            for z in range(cube.shape[2]):
                x_start = x_intervals[x] + 1
                y_start = y_intervals[y] + 1
                z_start = z_intervals[z] + 1
                x_end = x_intervals[x + 1] - 1
                y_end = y_intervals[y + 1] - 1
                z_end = z_intervals[z + 1] - 1
                if x_intervals[x] == x_intervals[x + 1]:
                    x_start = x_intervals[x]
                    x_end = x_intervals[x + 1]
                elif x_start > x_end:
                    continue
                if y_intervals[y] == y_intervals[y + 1]:
                    y_start = y_intervals[y]
                    y_end = y_intervals[y + 1]
                elif y_start > y_end:
                    continue
                if z_intervals[z] == z_intervals[z + 1]:
                    z_start = z_intervals[z]
                    z_end = z_intervals[z + 1]
                elif z_start > z_end:
                    continue
                if cube[x, y, z] == 0:
                    mini_cube_coordinates = [
                        [x_start, x_end],
                        [y_start, y_end],
                        [z_start, z_end],
                    ]
                    volume -= get_volume(mini_cube_coordinates)
    return volume


def intersect_intervals(
    unchanged_interval: List[List[Union[int, float]]], cut_interval: List[List[int]]
) -> (Optional[List[List[int]]], Optional[List[List[int]]]):
    intersection_interval = [[] for _ in range(3)]
    for i in range(3):
        if (
            unchanged_interval[i][0] > cut_interval[i][1]
            or unchanged_interval[i][1] < cut_interval[i][0]
        ):
            return cut_interval

        intersection_interval[i].append(
            max(cut_interval[i][0], unchanged_interval[i][0])
        )
        intersection_interval[i].append(
            min(cut_interval[i][1], unchanged_interval[i][1])
        )

    if get_volume(intersection_interval) == get_volume(cut_interval):
        return None
    return cut_interval + intersection_interval


def light_cubes_inside_region(
    instructions: List[List[Union[int, List[int]]]],
    forbidden_intervals: List[List[List[Union[int, float]]]],
) -> List[List[List[int]]]:
    lit_intervals = []
    for i, instruction in enumerate(reversed(instructions)):
        cut_interval = [instruction[i] for i in range(1, 4)]
        if instruction[0] == 1:
            for forbidden_interval in forbidden_intervals:
                cut_interval = intersect_intervals(forbidden_interval, cut_interval)
                if cut_interval is None:
                    break
            for lit_interval in lit_intervals:
                if cut_interval is None:
                    break
                cut_interval = intersect_intervals(lit_interval[:3], cut_interval)

            if cut_interval is not None:
                lit_intervals.append(cut_interval)
        else:
            forbidden_intervals.append(cut_interval)
    return lit_intervals


def read_from_file(filename: str) -> List[List[Union[int, List[int]]]]:
    with open(filename) as f:
        data = [line.rstrip().split(" ") for line in f.readlines()]

    instructions = []
    for i, line in enumerate(data):
        instructions.append([])
        if line[0] == "on":
            instructions[i].append(1)
        else:
            instructions[i].append(0)
        line_part = [j.split("=") for j in line[1].split(",")]
        instructions[i].append(list(map(int, line_part[0][1].split(".."))))
        instructions[i].append(list(map(int, line_part[1][1].split(".."))))
        instructions[i].append(list(map(int, line_part[2][1].split(".."))))
    return instructions
