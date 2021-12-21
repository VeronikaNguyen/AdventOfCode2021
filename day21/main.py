import copy

from functions import (
    play_game_with_deterministic_dice,
    play_game_with_quantum_dice,
    read_from_file,
)


if __name__ == "__main__":
    positions = read_from_file("day21")

    print("Solution part 1:")
    print(play_game_with_deterministic_dice(copy.deepcopy(positions)))

    print("\nSolution part 2:")
    print(play_game_with_quantum_dice(positions))
