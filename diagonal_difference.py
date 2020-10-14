# HackerRank Challenge.
# Ahmed Amin 14 / 10 / 2020.

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix  is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9

# The left_to_right_diagonal = 1 + 5 + 9 = 15. (0-0)(1-1)(2-2)
# The right_to_left_diagonal = 3 + 5 + 9 = 17. (0-2)(1-1)(2-0)
# Their absolute difference is 15 - 17 = 2.
#
# Function description :
# Complete the  function in the editor below.
# diagonalDifference takes the following parameter:
# int arr[n][m]: an array of integers
# Return
# int: the absolute diagonal difference

def diagonal_difference(arr):
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    n = arr[0][0]
    new_arr = []

    for x in range(1, n + 1):
        print("x value: ", x)
        for y in range(n):
            # print("y value: ", y)
            new_arr.append(arr[x][y])

    for i in range(n):
        index = i * (n + 1)
        left_to_right_diagonal += new_arr[index]
    for i in range(1, n + 1):
        index = (n - 1) * i
        right_to_left_diagonal += new_arr[index]

    return abs(left_to_right_diagonal - right_to_left_diagonal)


array1 = [
    [3],
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

array2 = [
    [3],
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]

print(diagonal_difference(array1))
print(diagonal_difference(array2))

