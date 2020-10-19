# HackerRank Challenge.
# Ahmed Amin 19 / 10 / 2020.

# complicated but you can check the link
# https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=next-challenge&h_v=zen

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    available_apples = 0
    available_oranges = 0

    for i in range(len(apples)):
        current_location = apples[i] + a
        if s <= current_location <= t:
            available_apples += 1
    print(available_apples)
    for i in range(len(oranges)):
        current_location = oranges[i] + b
        if s <= current_location <= t:
            available_oranges += 1
    print(available_oranges)


apples_location = [-2, 2, 1]
oranges_location = [5, -6]
count_apples_and_oranges(7, 11, 5, 15, apples_location, oranges_location)
