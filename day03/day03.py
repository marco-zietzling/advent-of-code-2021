print("advent of code 2021 - day 3")


def count_zeros_ones_at_list_position(input_list, position):
    num_zeros = 0
    num_ones = 0

    for item in input_list:
        if item[position] == "0":
            num_zeros += 1
        elif item[position] == "1":
            num_ones += 1
        else:
            raise Exception(f"unknown number '{item[position]}' at position {position}")

    return num_zeros, num_ones


def keep_only_matching_numbers(input_list, position, criteria):
    result_list = list()

    for item in input_list:
        if item[position] == criteria:
            result_list.append(item)

    return result_list


binary_numbers = list()

with open("input.txt") as file:
    for line in file:
        binary_numbers.append(str(line).strip())

# part 1
gamma = ""
epsilon = ""

for i in range(len(binary_numbers[0])):
    num_ones, num_zeros = count_zeros_ones_at_list_position(binary_numbers, i)

    if num_ones > num_zeros:
        gamma += "1"
        epsilon += "0"
    elif num_ones < num_zeros:
        gamma += "0"
        epsilon += "1"
    else:
        raise Exception("non deterministic logic detected: number of ones equals number of zeros")

# result = 3912944
print(f"part 1: {int(gamma, 2) * int(epsilon, 2)}")

# part 2
oxygen_generator_candidates = binary_numbers[:]
co2_scrubber_candidates = binary_numbers[:]

for i in range(len(oxygen_generator_candidates[0])):

    num_zeros, num_ones = count_zeros_ones_at_list_position(oxygen_generator_candidates, i)

    if num_ones >= num_zeros:
        oxygen_generator_candidates = keep_only_matching_numbers(oxygen_generator_candidates, i, "1")
    else:
        oxygen_generator_candidates = keep_only_matching_numbers(oxygen_generator_candidates, i, "0")

    if len(oxygen_generator_candidates) == 1:
        break

for i in range(len(co2_scrubber_candidates[0])):

    num_zeros, num_ones = count_zeros_ones_at_list_position(co2_scrubber_candidates, i)

    if num_ones >= num_zeros:
        co2_scrubber_candidates = keep_only_matching_numbers(co2_scrubber_candidates, i, "0")
    else:
        co2_scrubber_candidates = keep_only_matching_numbers(co2_scrubber_candidates, i, "1")

    if len(co2_scrubber_candidates) == 1:
        break

# result = 4996233
print(f"part 2: {int(oxygen_generator_candidates[0], 2) * int(co2_scrubber_candidates[0], 2)}")
