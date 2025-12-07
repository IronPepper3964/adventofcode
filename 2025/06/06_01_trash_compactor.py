# https://adventofcode.com/2025/day/6
#
import re
import math

with open('2025/06/input/aoc06_01.txt', 'r') as file:
    puzzle_input = file.readlines()

puzzle_lines = []
operator_lines:list[str] = []

for p in puzzle_input[:-1]:
    puzzle_lines_tmp_list = re.sub('[" "]+', ",", p.strip()).split(",")
    for plt in puzzle_lines_tmp_list:
        plt = int(plt)
    puzzle_lines_int = [int(p) for p in puzzle_lines_tmp_list]
    puzzle_lines.append(puzzle_lines_int)

# Make the operator list
operator_lines = re.sub('[" "]+', ",", puzzle_input[-1].strip()).split(",")

assert len(operator_lines) == len(puzzle_lines[1])

def add_all(num_list) -> int:
    total = 0
    for n in num_list:
        total += n
    return total

def mult_all(num_list) -> int:
    total = math.prod(num_list)
    return total

grand_total:int = 0

prob_num:int = 0

for op in operator_lines:
    problem_num_list:list[int] = []

    for pl in puzzle_lines:
        problem_num_list.append(pl[prob_num])

    print(f"problem_num_list: {problem_num_list}")
    
    if op == "+":
        grand_total += add_all(problem_num_list)
    elif op == "*":
        grand_total += mult_all(problem_num_list)
    else:
        raise NotImplementedError("No Operator Avaiable")
    
    prob_num += 1

    print(grand_total)


print(f"grand_total: {grand_total}")