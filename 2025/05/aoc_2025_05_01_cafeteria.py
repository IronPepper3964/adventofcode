import logging
from typing import List, Tuple

######
## Generic AoC setup
######
use_example_input: bool = False

input_file_location: str = "2025/05/input/aoc_05.txt"
example_input_file_location: str = "2025/05/input/aoc_05_example.txt"
LOG_LEVEL = logging.INFO

logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


if use_example_input:
    with open(example_input_file_location, "r", encoding="utf-8") as file:
        puzzle_input = file.readlines()
else:
    with open(input_file_location, "r", encoding="utf-8") as file:
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
## The database operates on ingredient IDs.
## It consists of a list of fresh ingredient ID ranges, a blank line
## he fresh ID ranges are inclusive
###############

###############
## Strategy:
##
## * Break the puzzle_input into two Lists - one for ranges, one for IDs
## * Loop through th ids:
##    * If an id matches any range, return True, add it to the count.
###############

ingredient_ranges: List[Tuple[int,int]] = []
ingredients: List[int] = []
ing_ranges_complete: bool = False

for i in puzzle_input:
    if i == "":
        ing_ranges_complete = True
        continue

    if ing_ranges_complete:
        ingredients.append(int(i))
    else:
        logger.debug(i.find("-"))
        ingredient_ranges.append((int(i[:i.find("-")]),int(i[i.find("-")+1:])))

logger.debug(ingredient_ranges)
logger.debug("====================")
logger.debug(ingredients)

fresh_count:int = 0

for i in ingredients:
    ingreedient_is_fresh:bool = False

    if ingreedient_is_fresh:
        break

    for ir in ingredient_ranges:
        if i >= ir[0] and i <= ir[1]:
            ingreedient_is_fresh = True
            fresh_count += 1
            break

logger.info("Result: %s", fresh_count)

