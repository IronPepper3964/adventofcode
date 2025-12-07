# https://adventofcode.com/2025/day/6
#
import re
import math

with open('2025/06/input/aoc06_01.txt', 'r') as file:
    puzzle_input = file.readlines()

def add_all(num_list) -> int:
    total = 0
    for n in num_list:
        total += n
    return total

def mult_all(num_list) -> int:
    total = math.prod(num_list)
    return total

puzzle_lines = []
operator_lines:list[str] = re.sub('[" "]+', ",", puzzle_input[-1].strip()).split(",")

new_col:bool = False
cur_index:int = 0
grand_total:int = 0

for op in operator_lines:
    new_col = False
    cur_nums = []

    while not new_col:
        cur_digit_str = ""
        for p in puzzle_input[:-1]:
            tmp_digit = p[cur_index]
            if not tmp_digit == " ":
                cur_digit_str += tmp_digit

        print(cur_digit_str)
        cur_index += 1
        if not cur_digit_str.strip() == "":
            cur_nums.append(int(cur_digit_str))
        else:
            new_col = True

    #Calculate math
    if op == "+":
        grand_total += add_all(cur_nums)
    elif op == "*":
        grand_total += mult_all(cur_nums)
    else:
        raise NotImplementedError("No Operator Avaiable")
    # Calculate grand totals
    print(grand_total)

print(f"Final Grand Total: {grand_total}")