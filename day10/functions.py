from typing import List


def count_completion_score(brackets: List[str]) -> int:
    completion_score = []
    for line in brackets:
        score = 0
        brackets_stack = []
        for letter in line:
            if letter == "<" or letter == "{" or letter == "[" or letter == "(":
                brackets_stack.append(letter)
            else:
                brackets_stack.pop()
        while len(brackets_stack) > 0:
            letter = brackets_stack.pop()
            score *= 5
            if letter == "(":
                score += 1
            elif letter == "[":
                score += 2
            elif letter == "{":
                score += 3
            elif letter == "<":
                score += 4
        completion_score.append(score)
    completion_score.sort()
    return completion_score[len(completion_score) // 2]


def count_syntax_error_score(brackets: List[str]) -> (int, List[str]):
    error_score = 0
    incomplete_brackets = []
    for line in brackets:
        incomplete = True
        brackets_stack = []
        for letter in line:
            if letter == "<" or letter == "{" or letter == "[" or letter == "(":
                brackets_stack.append(letter)
            else:
                last_element = brackets_stack.pop()
                if map_brackets(letter) != last_element:
                    if letter == ")":
                        error_score += 3
                    elif letter == "]":
                        error_score += 57
                    elif letter == "}":
                        error_score += 1197
                    elif letter == ">":
                        error_score += 25137
                    incomplete = False
                    break
        if incomplete:
            incomplete_brackets.append(line)
    return error_score, incomplete_brackets


def map_brackets(letter: str) -> str:
    if letter == ">":
        return "<"
    elif letter == "}":
        return "{"
    elif letter == "]":
        return "["
    elif letter == ")":
        return "("


def read_from_file(filename: str) -> List[str]:
    with open(filename) as f:
        brackets = [line.rstrip() for line in f]
    return brackets
