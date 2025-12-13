# https://adventofcode.com/2025/day/1
#
# Rules:
# Dial starts at 50
# `L` lines decrease the number
# `R` lines increase the number
# 0 is the minimum number, 99 is the max, numbers roll over

use_example_input: bool = False

if use_example_input:
    with open("2025/01/input/aoc01_example.txt", "r") as file:
        puzzle_input = file.readlines()
else:
    with open("2025/01/input/aoc01_01.txt", "r") as file:
        puzzle_input = file.readlines()


def parse_rotation(rotation: str):
    return (rotation[0], (int(int(rotation[1:]) / 100)), (int(rotation[1:]) % 100))


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
previous_position: int = current_position

for rotation in puzzle_input:
    previous_position = current_position
    # Get the rotation amount from the line:
    (rotation_dir, rotation_count, rotation_remainder_amount) = parse_rotation(rotation)

    print(
        f"rotation: {rotation} | rotation_dir:{rotation_dir} |  rotation_count:{rotation_count} |  rotation_remainder_amount:{rotation_remainder_amount}"
    )

    # Add full rotations
    zero_count += rotation_count

    if rotation_dir.upper() == "L":
        rotation_remainder_amount = -rotation_remainder_amount

    current_position = current_position + rotation_remainder_amount

    # determine if 0 was passed
    if (current_position > 99 or current_position <= 0) and not previous_position == 0:
        zero_count += 1

    current_position = rollover_adjust(current_position)

    print(
        f"Current Position: {current_position} | rotation: {rotation_remainder_amount} | zero_count: {zero_count} | Input: {rotation[:-1]}"
    )

print(f"Solution: {zero_count}")
