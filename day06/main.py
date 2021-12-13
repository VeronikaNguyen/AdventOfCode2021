from functions import (
    read_from_file,
    simulate_lanternfish_population,
)

if __name__ == "__main__":
    population_timer = read_from_file("day6")

    print("Solution part 1:")
    print(simulate_lanternfish_population(population_timer, 80))

    print("\nSolution part 2:")
    print(simulate_lanternfish_population(population_timer, 256))
