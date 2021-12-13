from collections import defaultdict
import copy
from typing import Dict
from typing import List
from typing import Set


def DFS(
    current_node: str,
    paths: Dict[str, List],
    paths_counter: int,
    visited_nodes: Set[str]
) -> int:
    if current_node.islower():
        visited_nodes.add(current_node)
    if current_node == "end":
        paths_counter += 1
        return paths_counter
    for neighbour in paths[current_node]:
        if neighbour not in visited_nodes:
            paths_counter = DFS(
                neighbour,
                paths,
                paths_counter,
                copy.deepcopy(visited_nodes),
            )
    return paths_counter


def DFS_visiting_small_caves_twice(
    current_node: str,
    paths: Dict[str, List],
    paths_counter: int,
    visited_nodes: Set[str],
    small_cave_visited_twice: bool
) -> int:
    if current_node.islower():
        visited_nodes.add(current_node)
    if current_node == "end":
        paths_counter += 1
        return paths_counter
    for neighbour in paths[current_node]:
        if neighbour not in visited_nodes:
            paths_counter = DFS_visiting_small_caves_twice(
                neighbour,
                paths,
                paths_counter,
                copy.deepcopy(visited_nodes),
                small_cave_visited_twice
            )
        elif not small_cave_visited_twice and neighbour != "start":
            paths_counter = DFS_visiting_small_caves_twice(
                neighbour,
                paths,
                paths_counter,
                copy.deepcopy(visited_nodes),
                True
            )
    return paths_counter


def count_paths(paths: Dict[str, List]) -> int:
    paths_counter = 0
    visited_nodes = set()
    paths_counter = DFS("start", paths, paths_counter, visited_nodes)
    return paths_counter


def count_paths_visiting_small_cave_twice(paths: Dict[str, List]) -> int:
    paths_counter = 0
    visited_nodes = set()
    paths_counter = DFS_visiting_small_caves_twice(
        "start", paths, paths_counter, visited_nodes, False
    )
    return paths_counter


def read_from_file(filename: str) -> Dict[str, List]:
    with open(filename) as f:
        path_data = [line.rstrip().split("-") for line in f]
    paths = defaultdict(list)
    for edge in path_data:
        if edge[0] == "start":
            paths[edge[0]].append(edge[1])
        elif edge[1] == "end":
            paths[edge[0]].append(edge[1])
        else:
            paths[edge[0]].append(edge[1])
            paths[edge[1]].append(edge[0])
    return paths
