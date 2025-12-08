# https://adventofcode.com/2025/day/7

# The resurcive code below may eventually work, but it was stopped after multiple hours without notable progress.
# Either there is a bug, or the real soltion is math based.

from typing import List

with open('2025/07/input/aoc07_01.txt', 'r') as file:
    puzzle_input = file.readlines()

puzzle_input_cleaned = [p.strip() for p in puzzle_input]
[print(p) for p in puzzle_input_cleaned]
print("")

split_count:int = 0

max_col:int = 0

def recursivly_get_timeline_count(puzzle_text:List[str], row_num:int = 1) -> int:
    #Pass in the current puzzle text and row number
    # Expected that the first time will be left, then second time will be right.

    timeline_count:int = 0
    
    # Break the loop if the row number is outsid eof the bounds of the puzzle text - return '1' as this is the end of a single timeline
    if len(puzzle_text) <= row_num:
        return 1

    #Else, continue on to find all timelines

    #Get the row above
    prev_row = puzzle_text[row_num-1]
    cur_row = puzzle_text[row_num]

    # find the previous lazer
    prev_row = prev_row.replace("S", "|")
    index:int = prev_row.find("|")

    cur_cell = cur_row[index]
    cur_row_start_str = cur_row.split()

    #print(cur_cell) 

    # Calculate the lasers next move on the current row
    replacement_row = ""
    if cur_cell == ".":
        new_puzzle_text = puzzle_text.copy()
        new_puzzle_text[row_num] = cur_row[:index] + "|" + cur_row[index+1:]
        timeline_count += recursivly_get_timeline_count(new_puzzle_text, row_num=row_num+1)
    elif cur_cell == "^":
        new_puzzle_text = puzzle_text.copy()
        new_puzzle_text[row_num] = cur_row[:index-1] + "|^" + cur_row[index+1:]
        timeline_count += recursivly_get_timeline_count(new_puzzle_text, row_num=row_num+1)
        new_puzzle_text = puzzle_text.copy()
        new_puzzle_text[row_num] = cur_row[:index] + "^|" + cur_row[index+1:]
        timeline_count += recursivly_get_timeline_count(new_puzzle_text, row_num=row_num+1)

    if index > 50 and index%5==0:
        print(index)
    return timeline_count

print(recursivly_get_timeline_count(puzzle_input_cleaned))
quit()