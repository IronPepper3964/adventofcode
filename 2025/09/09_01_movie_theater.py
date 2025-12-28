import logging
from pathlib import Path

######
## Generic AoC setup
######

log_level = logging.INFO
logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

use_example_input: bool = False

puzzle_input_path: Path = Path()
if use_example_input:
    puzzle_input_path = Path("2025/09/input/aoc09_example.txt")
else:
    puzzle_input_path = Path("2025/09/input/aoc09.txt")

with puzzle_input_path.open("r") as file:
    puzzle_input = file.readlines()


def clean_input_lines(in_puzzle_input: list[str]) -> list[str]:
    return [x.strip() for x in in_puzzle_input]


puzzle_input = clean_input_lines(puzzle_input)

logger.debug(puzzle_input)

###############
## Problem:
##
## The input is a set of tile coordiantes.
##
## You can create rectangles by selecting any two tiles to be the opposite corners.
##
## What is the largest area of any rectangle you can make?
###############

###############
## Strategy:
##
## * Create a method that takes in two coorinantes and returns the area
## * Loop through the list of coordinates,
##      keeping track of the pair that make the largest area.
###############


def coordinates_to_area(
    in_coord_1: tuple[int, int],
    in_coord_2: tuple[int, int],
) -> int:
    return (abs(in_coord_1[0] - in_coord_2[0]) + 1) * (
        abs(in_coord_1[1] - in_coord_2[1]) + 1
    )


def string_coord_to_tuple(in_str: str) -> tuple[int, int]:
    tmp_coord = in_str.split(",")
    return (int(tmp_coord[0]), int(tmp_coord[1]))


max_area: int = -1
for i, t1 in enumerate(puzzle_input):
    for t2 in puzzle_input[i + 1 :]:
        area = coordinates_to_area(string_coord_to_tuple(t1), string_coord_to_tuple(t2))
        max_area = max(max_area, area)
        logger.debug("%s: %s - %s | %s", i, t1, t2, area)

logger.info("Max Area: %s", max_area)
