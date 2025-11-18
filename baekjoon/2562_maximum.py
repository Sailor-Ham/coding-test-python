import sys

read = sys.stdin.readline
INPUT_SIZE = 9
number_array = []

for i in range(INPUT_SIZE):
    number = int(read())
    number_array.append(number)

max_num = 0
max_num_index = 0
index = 0

for number in number_array:
    if number > max_num:
        max_num = number
        max_num_index = index

    index += 1

print(max_num)
print(max_num_index + 1)