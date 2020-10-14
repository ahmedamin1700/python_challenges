# HackerRank Challenge.
# Ahmed Amin 14 / 10 / 2020.

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the
# decimal value of each fraction on a new line with 6 places after the decimal.

def plus_minus(arr):
    positive = 0
    negative = 0
    zeros = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        elif arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1

    print("{:.6f}".format(positive / len(arr)))
    print("{:.6f}".format(negative / len(arr)))
    print("{:.6f}".format(zeros / len(arr)))


array = [-4, 3, -9, 0, 4, 1]
plus_minus(array)
