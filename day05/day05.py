print("advent of code 2021 - day 5")


def print_sea_ground(sea_ground):
    for row in range(size):
        print(f"{sea_ground[row]}")


def mark_vertical_line(sea_ground, x, y1, y2):
    if y1 > y2:
        (y1, y2) = (y2, y1)

    for i in range(y1, y2 + 1):
        sea_ground[i][x] += 1


def mark_horizontal_line(sea_ground, x1, x2, y):
    if x1 > x2:
        (x1, x2) = (x2, x1)

    for i in range(x1, x2 + 1):
        sea_ground[y][i] += 1


def mark_diagonal_line(sea_ground, x1, x2, y1, y2):
    x_path = 1
    y_path = 1
    if x1 > x2:
        x_path = -1
    if y1 > y2:
        y_path = -1

    diff = abs(x1 - x2)
    for i in range(diff + 1):
        x = x1 + (i * x_path)
        y = y1 + (i * y_path)
        sea_ground[y][x] += 1


def count_overlaps(sea_ground):
    overlap_counter = 0

    for row in range(size):
        for col in range(size):
            if sea_ground[row][col] >= 2:
                overlap_counter += 1

    return overlap_counter


vents = list()

with open("input.txt") as file:
    for line in file:
        vents.append(str(line).strip())

size = 1000
sea_ground = [[0 for col in range(size)] for row in range(size)]

for vent in vents:
    coord_start, coord_end = list(map(str, vent.split(" -> ")))
    x1, y1 = list(map(int, coord_start.split(",")))
    x2, y2 = list(map(int, coord_end.split(",")))

    if x1 == x2:
        mark_vertical_line(sea_ground, x1, y1, y2)
    elif y1 == y2:
        mark_horizontal_line(sea_ground, x1, x2, y1)
    else:
        pass

# print_sea_ground(sea_ground)

# result = 5774
print(f"part 1: {count_overlaps(sea_ground)}")

sea_ground = [[0 for col in range(size)] for row in range(size)]

for vent in vents:
    coord_start, coord_end = list(map(str, vent.split(" -> ")))
    x1, y1 = list(map(int, coord_start.split(",")))
    x2, y2 = list(map(int, coord_end.split(",")))

    if x1 == x2:
        mark_vertical_line(sea_ground, x1, y1, y2)
    elif y1 == y2:
        mark_horizontal_line(sea_ground, x1, x2, y1)
    else:
        mark_diagonal_line(sea_ground, x1, x2, y1, y2)

# result = 18423
print(f"part 2: {count_overlaps(sea_ground)}")
