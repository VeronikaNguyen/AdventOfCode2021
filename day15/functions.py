from queue import PriorityQueue

import numpy as np


def expand_the_map(risk_map: np.ndarray, expansion_rate: int) -> np.ndarray:
    expansion_map = np.zeros(
        (risk_map.shape[0] * expansion_rate, risk_map.shape[0] * expansion_rate),
        dtype=int,
    )
    for i in range(expansion_rate):
        for j in range(expansion_rate):
            expansion_map[
                i * risk_map.shape[0] : (i + 1) * risk_map.shape[0] :,
                j * risk_map.shape[1] : (j + 1) * risk_map.shape[1],
            ] = (risk_map + np.ones_like(risk_map) * (i + j)) // 10 + (
                (risk_map + np.ones_like(risk_map) * (i + j)) % 10
            )
    return expansion_map


def find_lowest_risk(risk_map: np.ndarray) -> int:
    queue = PriorityQueue()
    queue.put((risk_map[(1, 0)], (1, 0)))
    queue.put((risk_map[(0, 1)], (0, 1)))
    cumulated_risk = np.matrix(np.ones_like(risk_map) * np.inf)
    cumulated_risk[(0, 1)] = risk_map[(0, 1)]
    cumulated_risk[(1, 0)] = risk_map[(1, 0)]
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while not queue.empty():
        node = queue.get()[1]
        for d in neighbours:
            neighbour = (node[0] + d[0], node[1] + d[1])
            if (
                neighbour[0] != -1
                and neighbour[0] != risk_map.shape[0]
                and neighbour[1] != -1
                and neighbour[1] != risk_map.shape[1]
                and neighbour != (0, 0)
            ):
                if (
                    cumulated_risk[neighbour]
                    > cumulated_risk[node] + risk_map[neighbour]
                ):
                    cumulated_risk[neighbour] = (
                        cumulated_risk[node] + risk_map[neighbour]
                    )
                    queue.put((cumulated_risk[neighbour], neighbour))
    return int(cumulated_risk[-1, -1])


def read_from_file(filename: str) -> np.ndarray:
    with open(filename) as f:
        data = [line.rstrip() for line in f]
    risk_map = np.zeros((len(data), len(data[0])), dtype=int)
    for i, line in enumerate(data):
        risk_map[i, :] = list(map(int, list(line)))
    return risk_map
