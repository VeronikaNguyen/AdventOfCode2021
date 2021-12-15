from typing import List

import numpy as np


def count_dots_after_first_fold(
    paper: np.ndarray, folding_instructions: List[str]
) -> int:
    paper = fold_paper(paper, *folding_instructions[0])

    counter = 0
    for i in range(paper.shape[0]):
        for j in range(paper.shape[1]):
            if paper[i, j] >= 1:
                counter += 1
    return counter


def determine_code(paper: np.ndarray, folding_instructions: List[str]) -> str:
    for instruction in folding_instructions:
        paper = fold_paper(paper, *instruction)
    paper = paper.T
    code = ""
    for i in range(paper.shape[0] - 1, -1, -1):
        for j in range(paper.shape[1] - 1, -1, -1):
            if paper[i, j] >= 1:
                code += "#"
            else:
                code += "."
        code += "\n"
    return code


def fold_paper(paper: np.ndarray, fold_axis: str, fold_idx: int) -> np.ndarray:
    fold_idx = int(fold_idx)
    if fold_axis == "y":
        paper = paper.T

    folded_paper = np.zeros(
        (max(fold_idx, paper.shape[0] - fold_idx), paper.shape[1]), dtype=int
    )

    if folded_paper.shape[0] == fold_idx:
        folded_paper = paper[:fold_idx, :]
        for i in range(fold_idx + 1, paper.shape[0]):
            folded_paper[fold_idx - i, :] += paper[i, :]
    else:
        folded_paper = paper[fold_idx + 1 :, :]
        for i in range(fold_idx):
            folded_paper[i, :] += paper[fold_idx - i - 1, :]

    if fold_axis == "y":
        folded_paper = folded_paper.T
    return folded_paper


def read_from_file(filename: str) -> (np.ndarray, List[str]):
    with open(filename) as f:
        data = [line.rstrip().split(",") for line in f]

    fold_instructions = []
    dots = []
    max_x, max_y = 0, 0
    instructions = False
    for line in data:
        if instructions:
            fold_instructions.append(line[0].split(" ")[-1].split("="))
        elif len(line) == 2:
            dots.append((int(line[0]), int(line[1])))
            if dots[-1][0] > max_x:
                max_x = dots[-1][0]
            if dots[-1][1] > max_y:
                max_y = dots[-1][1]
        else:
            instructions = True

    paper = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for dot in dots:
        paper[dot[0], dot[1]] = 1
    return paper, fold_instructions
