print("advent of code 2021 - day 1")

entries = list()

with open("input.txt") as file:
    for line in file:
        entries.append(int(line))

# part 1
current_depth = entries[0]
num_depth_measurement_increases = 0

for entry in entries:
    if entry > current_depth:
        num_depth_measurement_increases += 1

    current_depth = entry

print(f"part 1: result = {num_depth_measurement_increases}")

# part 2
current_window_depth = entries[0] + entries[1] + entries[2]
num_depth_measurement_increases = 0

for i in range(0, len(entries) - 2):
    next_window_depth = entries[i] + entries[i + 1] + entries[i + 2]

    if next_window_depth > current_window_depth:
        num_depth_measurement_increases += 1

    current_window_depth = next_window_depth

print(f"part 2: result = {num_depth_measurement_increases}")
