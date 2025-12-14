import math
import logging

log_level = logging.INFO

logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


use_example_input: bool = False

if use_example_input:
    with open("2025/02/input/aoc02_example.txt", "r") as file:
        puzzle_input = file.readlines()
else:
    with open("2025/02/input/aoc02.txt", "r") as file:
        puzzle_input = file.readlines()


def is_sequence_duplicated(sequence: str, in_str: str) -> bool:
    logger.debug(f"sequence: {sequence} | in_str: {in_str}")
    logger.debug(f"{sequence} == {in_str[len(sequence):len(sequence)*2]}")

    seq_len = len(sequence)
    str_len = len(in_str)
    seq_count = math.ceil(str_len/seq_len)
    
    for i in range(1,seq_count):
        tmp_start = seq_len * i
        logger.debug(f"{'matches' if sequence == in_str[tmp_start:(tmp_start+seq_len)] else 'no match'} | {sequence} != in_str[{tmp_start}:{(tmp_start+seq_len)}] | {in_str[tmp_start:(tmp_start+seq_len)]}")

        if sequence != in_str[tmp_start:(tmp_start+seq_len)]:
            return False
    return True


def has_repeated_sequence(in_id: str):
    id_half_len = int(len(in_id) / 2)

    for i in range(1, id_half_len + 1):
        logger.debug(in_id[:i])
        if is_sequence_duplicated(in_id[:i],in_id):
            return True
    return False


id_range_list = str(puzzle_input[0]).split(",")

invalid_sum: int = 0

id_count:int = 0

for id_range in id_range_list:
    id_count += 1

    logger.debug(id_range)
    logger.debug(id_range.split("-"))

    if id_count%100:
        logger.info(f"ID row count: {id_count} | {len(id_range_list)}")

    for id in range(int(id_range.split("-")[0]), int(id_range.split("-")[1]) + 1):
        if has_repeated_sequence(str(id)):
            invalid_sum += id

logger.info(f"Solution: {invalid_sum}")
