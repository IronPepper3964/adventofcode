use_example_input: bool = False

if use_example_input:
    with open("2025/02/input/aoc02_example.txt", "r") as file:
        puzzle_input = file.readlines()
else:
    with open("2025/02/input/aoc02.txt", "r") as file:
        puzzle_input = file.readlines()

id_range_list = str(puzzle_input[0]).split(',')

invalid_sum:int = 0

for id_range in id_range_list:
    print(id_range)
    print(id_range.split('-'))

    for id in range(int(id_range.split('-')[0]), int(id_range.split('-')[1])+1):
        id_str = str(id)
        id_half_len = int(len(id_str)/2)
        half_id = id_str[:id_half_len]
        if half_id == id_str[id_half_len:]:
            invalid_sum += id
    pass

print(f"Solution: {invalid_sum}")