# https://adventofcode.com/2025/day/1
#
# Rules:
# Dial starts at 50
# `L` lines decrease the number
# `R` lines increase the number
# 0 is the minimum number, 99 is the max, numbers roll over

with open("2025/01/input/aoc01_01.txt", "r") as file:
    puzzle_input = file.readlines()


def parse_rotation(rotation: str):
    # Handle rotations over 100
    return (rotation[0], (int(rotation[1:]) % 100))


def rollover_adjust(position: int):
    if position >= 0 and position <= 99:
        return position

    if position < 0:
        position = 100 + position
    elif position > 99:
        position = position - 100

    return position


current_position: int = 50
zero_count: int = 0

for rotation in puzzle_input:
    # Get the rotation amount from the line:
    (rotation_dir, rotation_amount) = parse_rotation(rotation)

    if rotation_dir.upper() == "L":
        rotation_amount = -rotation_amount

    current_position = current_position + rotation_amount

    current_position = rollover_adjust(current_position)

    if current_position == 0:
        zero_count = zero_count + 1

    print(
        f"Current Position: {current_position} | rotation: {rotation_amount} | zero_count: {zero_count} | Input: {rotation[:-1]}"
    )

print(f"Solution: {zero_count}")
