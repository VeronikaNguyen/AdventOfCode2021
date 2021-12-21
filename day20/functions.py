import numpy as np


def apply_convolution(
    enhancement_instructions: str, image: np.ndarray, steps: int
) -> np.ndarray:
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    new_image = np.array(image)
    padding_constant = "0"
    for s in range(steps):
        print(s)
        image = np.array(new_image)
        image = np.pad(
            image, [(3, 3), (3, 3)], mode="constant", constant_values=padding_constant
        )
        new_image = np.array(image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                convolution = ""
                for d in directions:
                    if (
                        0 <= i + d[0] < image.shape[0]
                        and 0 <= j + d[1] < image.shape[1]
                    ):
                        convolution += str(image[i + d[0], j + d[1]])
                    else:
                        convolution += padding_constant
                new_image[i, j] = enhancement_instructions[int(convolution, 2)]
        if padding_constant == "0":
            padding_constant = enhancement_instructions[0]
        else:
            padding_constant = enhancement_instructions[2 ** 9 - 1]
    return new_image


def count_lit_pixels(
    enhancement_instructions: str, image: np.ndarray, steps: int
) -> int:
    new_image = apply_convolution(enhancement_instructions, image, steps)
    counter = 0
    for i in range(new_image.shape[0]):
        for j in range(new_image.shape[1]):
            if new_image[i, j] == 1:
                counter += 1
    return counter


def read_from_file(filename: str) -> (str, np.ndarray):
    with open(filename) as f:
        data = [line.rstrip() for line in f.readlines()]

    enhancement_instructions = ""
    for letter in data[0]:
        if letter == "#":
            enhancement_instructions += "1"
        else:
            enhancement_instructions += "0"

    image = np.zeros((len(data[2:]), len(data[2])), dtype=int)
    for i, line in enumerate(data[2:]):
        temp_line = ""
        for letter in line:
            if letter == "#":
                temp_line += "1"
            else:
                temp_line += "0"
        image[i] = list(temp_line)
    return enhancement_instructions, image
