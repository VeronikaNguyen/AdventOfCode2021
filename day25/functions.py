import numpy as np


def move_cucumbers(cucumbers: np.ndarray) -> (np.ndarray, bool):
    moved_east_cucumbers = np.zeros_like(cucumbers, dtype=int)
    moved = False
    for i in range(cucumbers.shape[0]):
        for j in range(cucumbers.shape[1]):
            if cucumbers[i, j] == 1 and cucumbers[i, (j + 1) % cucumbers.shape[1]] == 0:
                moved_east_cucumbers[i, (j + 1) % cucumbers.shape[1]] = 1
                moved = True
            elif cucumbers[i, j] == 1:
                moved_east_cucumbers[i, j] = 1
            elif cucumbers[i, j] == 2:
                moved_east_cucumbers[i, j] = 2

    moved_cucumbers = np.zeros_like(cucumbers, dtype=int)
    for i in range(cucumbers.shape[0]):
        for j in range(cucumbers.shape[1]):
            if (
                cucumbers[i, j] == 2
                and moved_east_cucumbers[(i + 1) % cucumbers.shape[0], j] == 0
            ):
                moved_cucumbers[(i + 1) % cucumbers.shape[0], j] = 2
                moved = True
            elif cucumbers[i, j] == 2:
                moved_cucumbers[i, j] = 2
            elif moved_east_cucumbers[i, j] == 1:
                moved_cucumbers[i, j] = 1
    return moved_cucumbers, moved


def determine_cucumbers_stop(cucumbers: np.ndarray) -> int:
    moved = True
    steps = 0
    while moved:
        steps += 1
        cucumbers, moved = move_cucumbers(cucumbers)
    return steps


def read_from_file(filename: str) -> np.ndarray:
    with open(filename) as f:
        data = [line.rstrip() for line in f.readlines()]

    cucumbers = np.zeros(shape=(len(data), len(data[0])), dtype=int)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == ">":
                cucumbers[i, j] = 1
            elif data[i][j] == "v":
                cucumbers[i, j] = 2
    return cucumbers
