print("advent of code 2021 - day 2")

commands = list()

with open("input.txt") as file:
    for line in file:
        commands.append(str(line))

# part 1
horizontal_pos = 0
depth = 0

for command in commands:
    (action, attribute) = command.split(" ")

    if action == "up":
        depth -= int(attribute)
    elif action == "down":
        depth += int(attribute)
    elif action == "forward":
        horizontal_pos += int(attribute)
    else:
        print(f"unknown command {action} {attribute}")

# result = 1714950
print(f"part 1: result = {depth * horizontal_pos}")

# part 2
horizontal_pos = 0
depth = 0
aim = 0

for command in commands:
    (action, attribute) = command.split(" ")

    if action == "up":
        aim -= int(attribute)
    elif action == "down":
        aim += int(attribute)
    elif action == "forward":
        horizontal_pos += int(attribute)
        depth += aim * int(attribute)
    else:
        print(f"unknown command {action} {attribute}")

# result = 1281977850
print(f"part 2: result = {depth * horizontal_pos}")
