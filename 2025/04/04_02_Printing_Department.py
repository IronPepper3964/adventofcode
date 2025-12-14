import logging
from typing import List, Tuple

######
## Generic AoC setup
######

log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

use_example_input: bool = False

if use_example_input:
    with open("2025/04/input/aoc04_example.txt", "r") as file:
        puzzle_input = file.readlines()
else:
    with open("2025/04/input/aoc04.txt", "r") as file:
        puzzle_input = file.readlines()


def clean_input_lines(in_puzzle_input) -> List[str]:
    cleaned_input: List[str] = []
    for i in in_puzzle_input:
        cleaned_input.append(i.strip())
    return cleaned_input


puzzle_input = clean_input_lines(puzzle_input)

logger.debug(puzzle_input)

###############
## Problem:
##
## The forklifts can only access a roll of paper if there are
## fewer than four rolls of paper in the eight adjacent positions.
## How many rolls of paper can be accessed by a forklift?
##
## Once a roll of paper can be accessed by a forklift, it can be removed.
###############

###############
## Strategy:
##
## * Change the puzzle_input into a 2D list of characters.
## * Create a function that takes in the current x/y coordinate and then checks surrounding spaces
##     to count the `@` symbol counts
## * Loop through all locations with an `@` to count the number that can be moved
##
## Part 2 changes:
## Since the base code exists and efficiency isn't a goal - this can be solved by
## * Updating the puzzle_input after each loop where a roll is removed
## * continuing to itterate over the entire process until
##     no rolls have been removed after a full pass
###############


def puzzle_input_to_2d_list(in_puzzle_input: List[str]) -> List[List[str]]:
    return_puzzle_input: List[List[str]] = [[]]
    return_puzzle_input.clear()

    for r in in_puzzle_input:
        pir: List[str] = []
        for c in r:
            pir.append(c)
        return_puzzle_input.append(pir)

    return return_puzzle_input


def remove_roll_from_puzzle_input(
    x: int, y: int, in_puzzle_input: List[List[str]]
) -> List[List[str]]:
    return_puzzle_input: List[List[str]] = [[]]
    return_puzzle_input.clear()

    for r, row in enumerate(in_puzzle_input):
        for c, col in enumerate(row):
            if r == x and c == y:
                # Remove the roll
                row[c] = "."
        return_puzzle_input.append(row)

    return return_puzzle_input


def get_adjacent_roll_count(x: int, y: int, in_puzzle_input: List[List[str]]) -> int:
    adjacent_roll_count: int = 0
    for curr_x in range(x - 1, x + 2):
        for curr_y in range(y - 1, y + 2):
            # Avoid checking the center square
            if curr_x == x and curr_y == y:
                continue
            # Avoid going outside the index bounds
            if curr_x < 0 or curr_y < 0:
                continue
            if curr_x >= len(in_puzzle_input) or curr_y >= len(in_puzzle_input[x]):
                continue

            # Safe to count this coordinate
            logger.debug(
                "curr_x:%s | curr_y:%s | %s",
                curr_x,
                curr_y,
                in_puzzle_input[curr_x][curr_y],
            )

            if in_puzzle_input[curr_x][curr_y] == "@":
                adjacent_roll_count += 1
    return adjacent_roll_count


puzzle_input = puzzle_input_to_2d_list(puzzle_input)

logger.debug(get_adjacent_roll_count(0, 0, puzzle_input))

# Main loop
movable_roll_count: int = 0
roll_removed: bool = True

while roll_removed:
    roll_removed = False
    for r, row in enumerate(puzzle_input):
        logger.debug("row: %s | %s", r, row)
        for c, col in enumerate(row):
            logger.debug("col: %s | %s", c, col)
            if col != "@":
                continue
            if get_adjacent_roll_count(r, c, puzzle_input) < 4:
                movable_roll_count += 1
                remove_roll_from_puzzle_input(r, c, puzzle_input)
                roll_removed = True

logger.info("Result: %s", movable_roll_count)
