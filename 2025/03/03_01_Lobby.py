import logging
from typing import List, Tuple

log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

use_example_input: bool = False

if use_example_input:
    with open("2025/03/input/aoc03_example.txt", "r") as file:
        puzzle_input = file.readlines()
else:
    with open("2025/03/input/aoc03.txt", "r") as file:
        puzzle_input = file.readlines()


def clean_input_lines(puzzle_input) -> List[str]:
    cleaned_input: List[str] = []
    for i in puzzle_input:
        cleaned_input.append(i.strip())
    return cleaned_input


puzzle_input = clean_input_lines(puzzle_input)

###############
## Problem:
##
## each line of digits in your input corresponds to a single bank of batteries.
## Within each bank, you need to turn on exactly two batteries;
## the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on.
## For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)
###############

###############
## Strategy:
##
## Loop through each row twice:
##  * The first time, find the largest number.  If there is a tie - use the one furthest to the left.
##  * The second time, start at the index after the number selected above, then find the largest number
###############


def string_to_int_list(in_str: str) -> List[int]:
    int_list: List[int] = []
    for s in in_str:
        int_list.append(int(s))
    return int_list


def puzzle_input_to_int(puzzle_input_str: List[str]) -> List[List[int]]:
    # Change the puzzle input (list of strings) into a list of integer lists
    puzzle_input_int: List[List[int]] = []
    for row in puzzle_input_str:
        puzzle_input_int.append(string_to_int_list(row))
    return puzzle_input_int


def find_largest_int(in_list: List[int]) -> Tuple[int, int]:
    i = 0
    index_max: int = -1
    max_int: int = -1

    for c in in_list:
        if c > max_int:
            max_int = c
            index_max = i

        i += 1

    return (max_int, index_max)


puzzle_input = puzzle_input_to_int(puzzle_input)

total_joltage: int = 0

for r in puzzle_input:
    batt_1_val, batt_1_index = find_largest_int(r[:-1])
    logger.debug(f"{batt_1_val}|{batt_1_index}")
    batt_2_val, batt_2_index = find_largest_int(r[batt_1_index + 1 :])
    logger.debug(f"{batt_2_val}|{batt_2_index}")

    logger.debug(f"joltage: {(batt_1_val * 10) + batt_2_val}")
    total_joltage += (batt_1_val * 10) + batt_2_val

logger.info(f"Result: {total_joltage}")
