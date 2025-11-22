import sys

read = sys.stdin.readline

input_string = read().rstrip()

count_to_all_zero = 0
count_to_all_one = 0

if input_string[0] == '0':
    count_to_all_one += 1
elif input_string[0] == '1':
    count_to_all_zero += 1

for i in range(len(input_string) - 1):
    if input_string[i] != input_string[i + 1]:
        if input_string[i + 1] == '1':
            count_to_all_zero += 1
        elif input_string[i + 1] == '0':
            count_to_all_one += 1

print(min(count_to_all_zero, count_to_all_one))