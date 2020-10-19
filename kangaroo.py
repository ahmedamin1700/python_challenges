# HackerRank Challenge.
# Ahmed Amin 19 / 10 / 2020.

# Link to the challenge is https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        reminder = (x2 - x1) % (v1 - v2)
        if reminder == 0:
            return 'YES'
        else:
            return 'NO'
    return 'NO'


print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))
