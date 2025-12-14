import logging
from typing import List

######
## Generic AoC setup
######
use_example_input: bool = False

input_file_location:str = "[YYYY]/[DD]/input/aoc[DD].txt"
example_input_file_location:str = "[YYYY]/[DD]/input/aoc[DD]_example.txt"
LOG_LEVEL = logging.DEBUG

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


if use_example_input:
    with open(input_file_location, "r", encoding="utf-8") as file:
        puzzle_input = file.readlines()
else:
    with open(example_input_file_location, "r", encoding="utf-8") as file:
        puzzle_input = file.readlines()


def clean_input_lines(in_puzzle_input) -> List[str]:
    """Strips whitespace characters from all strings in the puzzle input."""
    cleaned_input: List[str] = []
    for i in in_puzzle_input:
        cleaned_input.append(i.strip())
    return cleaned_input


puzzle_input = clean_input_lines(puzzle_input)

logger.debug(puzzle_input)

###############
## Problem:
##
###############

###############
## Strategy:
##
###############
