# HackerRank Challenge.
# Ahmed Amin 18 / 10 / 2020.

# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year
# of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are
# tallest.

def birthday_cake_candles(candles):
    biggest = candles[0]
    count = 1

    for i in range(1, len(candles)):
        if candles[i] > biggest:
            biggest = candles[i]
        elif candles[i] == biggest:
            count += 1

    return count


array_candles1 = [4, 4, 1, 3]
array_candles2 = [3, 2, 3, 3]
print(birthday_cake_candles(array_candles1))
print(birthday_cake_candles(array_candles2))
