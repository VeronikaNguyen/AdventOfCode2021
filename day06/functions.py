from typing import Dict
from collections import defaultdict


def read_from_file(filename: str) -> Dict[int, int]:
    with open(filename) as f:
        population_timer_list = list(map(int, f.readline().rstrip().split(",")))
    population_timer = defaultdict(lambda: 0)
    for time in population_timer_list:
        population_timer[time] += 1
    return population_timer


def simulate_lanternfish_population(population_timer: Dict[int, int], time: int) -> int:
    for _ in range(time):
        new_population_timer = defaultdict(lambda: 0)
        for t in range(9):
            if t == 0:
                new_population_timer[6] += population_timer[0]
                new_population_timer[8] += population_timer[0]
            else:
                new_population_timer[t - 1] += population_timer[t]
        population_timer = new_population_timer
    population = 0
    for t in range(9):
        population += population_timer[t]
    return population

