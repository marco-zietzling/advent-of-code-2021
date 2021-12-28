print("advent of code 2021 - day 4")

bingo_input = list()

with open("input.txt") as file:
    for line in file:
        bingo_input.append(str(line).strip())

numbers = list(map(int, bingo_input[0].split(",")))
boards = list()


def read_board(bingo_input, position):
    result = list()

    return result, position
