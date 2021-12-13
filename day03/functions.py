from typing import List


def life_support_rating(diagnostic_report: List[str]) -> int:
    len_entry = len(diagnostic_report[0])
    entries = diagnostic_report
    position = 0
    while len(entries) > 1:
        entries0, entries1 = [], []
        for entry in entries:
            if entry[position] == "0":
                entries0.append(entry)
            else:
                entries1.append(entry)
        if len(entries0) <= len(entries1):
            entries = entries1
        else:
            entries = entries0
        position = (position + 1) % len_entry
    oxygen_generator_rating = int(entries[0], 2)

    entries = diagnostic_report
    position = 0
    while len(entries) > 1:
        entries0, entries1 = [], []
        for entry in entries:
            if entry[position] == "0":
                entries0.append(entry)
            else:
                entries1.append(entry)
        if len(entries0) <= len(entries1):
            entries = entries0
        else:
            entries = entries1
        position = (position + 1) % len_entry
    co2_scrubber_rating = int(entries[0], 2)
    return oxygen_generator_rating * co2_scrubber_rating


def power_consumption(diagnostic_report: List[str]) -> int:
    binary_gamma_rate, binary_epsilon_rate = "", ""
    for position in range(len(diagnostic_report[0])):
        count = 0
        for entry in diagnostic_report:
            if entry[position] == "1":
                count += 1
        if count > len(diagnostic_report) / 2:
            binary_gamma_rate += "1"
            binary_epsilon_rate += "0"
        else:
            binary_gamma_rate += "0"
            binary_epsilon_rate += "1"
    gamma_rate, epsilon_rate = int(binary_gamma_rate, 2), int(binary_epsilon_rate, 2)
    return gamma_rate * epsilon_rate


def read_from_file(filename: str) -> List[str]:
    with open(filename) as f:
        diagnostic_report = [line.rstrip() for line in f]
    return diagnostic_report
