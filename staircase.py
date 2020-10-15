# HackerRank Challenge.
# Ahmed Amin 15 / 10 / 2020.

# Staircase detail
#
# This is a staircase of size: n = 4.
#
#    #
#   ##
#  ###
# ####
#
# Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not
# preceded by any spaces.
# Write a program that prints a staircase of size.

def staircase(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        print(spaces + hashes)


staircase(4)
staircase(5)
