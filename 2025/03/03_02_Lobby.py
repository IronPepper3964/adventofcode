import logging
from typing import List, Tuple

log_level = logging.DEBUG
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
## The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; 
## the only difference is that now there will be 12 digits in each bank's joltage output instead of two.
###############

###############
## Strategy:
##
## Adjust the previous loop to handle arbitry number of batteries instead of hard coding logic for just 2
##  * The list index sent to `find_largest_int(..)` should remove n elemnts from the end of the list where n is the number of batteries remaining to be selected after this round
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

batteries_to_use:int = 12
total_joltage: int = 0

for r in puzzle_input:
    battery_joltages:str = ""
    start_index:int = 0
    battery_count:int = len(r)
    #TODO: Cleanup this for loop so it is more clear
    for b in range(batteries_to_use-1,-1,-1):
        if b > 0:
            batt_val, batt_index = find_largest_int(r[start_index:-b])
        else:
            batt_val, batt_index = find_largest_int(r[start_index:])

        logger.debug(f"{batt_val}|{batt_index}")
        battery_joltages = battery_joltages + str(batt_val)
        start_index += batt_index+1

    total_joltage += int(battery_joltages)

    logger.debug(f"battery bank total_joltage: {battery_joltages}")

logger.info(f"Result: {total_joltage}")
