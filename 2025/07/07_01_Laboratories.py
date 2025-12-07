# https://adventofcode.com/2025/day/7

with open('2025/07/input/aoc07_01.txt', 'r') as file:
    puzzle_input = file.readlines()

puzzle_input_cleaned = [p.strip() for p in puzzle_input]
[print(p) for p in puzzle_input_cleaned]
print("")

puzzle_output = []
puzzle_output.append(puzzle_input_cleaned[0])

split_count:int = 0

row:int = 0

def merge_new_and_old_line(new_line, old_line) -> str:
    out_str = ""

    for i in range(0, len(new_line)):
        if new_line[i]=="|":
            out_str = out_str + "|"
        else:
            out_str = out_str + old_line[i]
    return out_str

for li in range (1,len(puzzle_input_cleaned)):
    new_line = []

    for i in range(0, len(puzzle_input_cleaned[li])):
        if len(new_line)-1 >= i and new_line[i] == "|":
            pass
        elif puzzle_input_cleaned[li][i] == "^":
            if puzzle_input_cleaned[li-1][i] == "|":
                new_line[-1] = "|"
                new_line.append("^")
                new_line.append("|")
                split_count += 1
            else:
                new_line.append(puzzle_input_cleaned[li][i])
        elif puzzle_input_cleaned[li][i] == "." and puzzle_input_cleaned[li-1][i] in ["S", "|"]:
            new_line.append("|")
        else:
            new_line.append(puzzle_input_cleaned[li][i])

        if len(new_line)-1 - i < -1 or len(new_line)-1 - i > 1:
            pass

    puzzle_input_cleaned[li] = "".join(new_line)

    [print(p) for p in puzzle_input_cleaned]
    print("----------")

        

print(split_count)

