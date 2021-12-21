from collections import defaultdict
from typing import DefaultDict
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

import numpy as np
from scipy.spatial.transform import Rotation as R


def align_scanner(
    start_idx: int, scanner_list: List[np.ndarray]
) -> (int, Dict[int, np.ndarray]):
    remaining_scanners = set(i for i in range(0, len(scanner_list))) - {start_idx}
    scanner_dict = {start_idx: scanner_list[start_idx]}
    scanner_positions = {start_idx: np.array([0, 0, 0], dtype=int)}
    beacons = set()
    while len(remaining_scanners) > 0:
        found = False
        for i in list(remaining_scanners):
            for j in scanner_dict.keys():
                scanner1 = scanner_dict[j]
                scanner2 = scanner_list[i]
                new_beacons, scanner2, scanner2_position = align_scanner_pair(
                    scanner1, scanner2, scanner_positions[j]
                )
                if scanner2_position is not None:
                    scanner_dict[i] = scanner2
                    scanner_positions[i] = scanner2_position
                    beacons = beacons.union(new_beacons)
                    remaining_scanners.remove(i)
                    found = True
                    break
            if found:
                break
    return len(beacons), scanner_positions


def align_scanner_pair(
    scanner1: np.ndarray,
    scanner2: np.ndarray,
    scanner1_position: np.ndarray,
) -> (Set[Tuple[int, int, int]], np.ndarray, Optional[np.ndarray]):
    possible_rotations = [
        np.array([0, 0, 0, 1]),
        np.array([0, 1, 0, 1]),
        np.array([0, 1, 0, 0]),
        np.array([0, -1, 0, 1]),
        np.array([0, 0, 1, 1]),
        np.array([1, 1, 1, 1]),
        np.array([1, 1, 0, 0]),
        np.array([-1, -1, 1, 1]),
        np.array([0, 0, -1, 1]),
        np.array([-1, 1, -1, 1]),
        np.array([-1, 1, 0, 0]),
        np.array([1, -1, -1, 1]),
        np.array([1, 0, 0, 1]),
        np.array([1, 1, -1, 1]),
        np.array([0, 1, -1, 0]),
        np.array([1, -1, 1, 1]),
        np.array([1, 0, 0, 0]),
        np.array([1, 0, -1, 0]),
        np.array([0, 0, 1, 0]),
        np.array([1, 0, 1, 0]),
        np.array([-1, 0, 0, 1]),
        np.array([-1, 1, 1, 1]),
        np.array([0, 1, 1, 0]),
        np.array([-1, -1, -1, 1]),
    ]

    beacons = set()
    for beacon in scanner1:
        beacon = beacon + scanner1_position
        beacons.add(tuple(map(round, beacon)))
    overlap = compare_distances(scanner1, scanner2)
    if len(overlap) >= 12:
        for rot in possible_rotations:
            rotated_beacons = apply_rotation(scanner2, rot)
            for indices in overlap:
                overlapping_beacons = 0
                aligned = True
                scanner2_position = (
                    scanner1[indices[0]]
                    - rotated_beacons[indices[1]]
                    + scanner1_position
                )
                scanned_beacons = rotated_beacons + scanner2_position

                for i in range(scanned_beacons.shape[0]):
                    if tuple(map(round, scanned_beacons[i])) in beacons:
                        overlapping_beacons += 1
                    elif (
                        np.absolute(scanned_beacons[i] - scanner1_position)
                        <= np.array([1000, 1000, 1000])
                    ).all():
                        aligned = False
                        break

                if aligned and overlapping_beacons >= 12:
                    for i in range(scanned_beacons.shape[0]):
                        beacons.add(tuple(map(round, scanned_beacons[i])))
                    scanner2 = apply_rotation(scanner2, rot)
                    return beacons, scanner2, scanner2_position
    return beacons, scanner2, None


def apply_rotation(scanner: np.ndarray, quaternion: np.ndarray) -> np.ndarray:
    r = R.from_quat(quaternion)
    scanner = np.around(r.apply(scanner))
    return scanner


def compare_distances(
    scanner1: np.ndarray, scanner2: np.ndarray
) -> Set[Tuple[int, int]]:
    scanner1_distances = compute_scanner_distances(scanner1)
    scanner2_distances = compute_scanner_distances(scanner2)
    overlap = set()
    for s1 in scanner1_distances.keys():
        for s2 in scanner2_distances.keys():
            if len(scanner1_distances[s1].intersection(scanner2_distances[s2])) >= 12:
                overlap.add((s1, s2))
    return overlap


def compute_scanner_distances(
    scanner: np.ndarray,
) -> DefaultDict[int, Set[Tuple[int, int, int]]]:
    distances = defaultdict(set)
    for i in range(scanner.shape[0]):
        for j in range(scanner.shape[0]):
            distance = np.absolute(scanner[i] - scanner[j]).sum()
            k = 0
            while (distance, k) in distances[i]:
                k += 1
            distances[i].add((distance, k))
    return distances


def determine_largest_manhattan_distance(
    scanner_positions: Dict[int, np.ndarray]
) -> int:
    largest_manhattan_distance = 0
    for key1 in scanner_positions.keys():
        for key2 in scanner_positions.keys():
            distance = np.absolute(
                scanner_positions[key1] - scanner_positions[key2]
            ).sum()
            if distance > largest_manhattan_distance:
                largest_manhattan_distance = distance
    return int(largest_manhattan_distance)


def read_from_file(filename: str) -> List[np.ndarray]:
    with open(filename) as f:
        data_list = [line.rstrip() for line in f]

    scanner_list = []
    for line in data_list:
        if line[:3] == "---":
            scanner_list.append([])
        elif line == "":
            scanner_list[-1] = np.array(scanner_list[-1], dtype=int)
        else:
            scanner_list[-1].append(list(map(int, line.split(","))))
    scanner_list[-1] = np.array(scanner_list[-1], dtype=int)
    return scanner_list
