# HackerRank Challenge.
# Ahmed Amin 18 / 10 / 2020.

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of
# the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
# long integers.

def mini_max_sum(arr):
    new_arr = arr
    new_arr.sort()
    minimum = 0
    maximum = 0

    for n in range(len(new_arr) - 1):
        minimum += new_arr[n]

    for n in range(1, len(new_arr)):
        maximum += new_arr[n]

    print(minimum, maximum)


array1 = [4, 3, 1, 2, 5]
array2 = [1, 3, 5, 7, 9]
mini_max_sum(array1)
mini_max_sum(array2)
