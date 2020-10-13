# HackerRank Challenge.
# Ahmed Amin 13 / 10 / 2020.

# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an
# array of integers representing the color of each sock, determine how many pairs of socks with matching colors there
# are.


def sock_merchant(n, ar):
    colors = []  # array to store each color dic.
    counter = 0  # counter tracker.

    # loop through the array and converted to array of dictionary and add matched key => boolean.
    for color in ar:
        colors.append({"color": color, "matched": False})

    # loop through the array like two dimension with conditions as below.
    for i in range(n):
        # first = colors[i]
        for y in range(1, n):
            # second = colors[y]
            if colors[i]["color"] == colors[y]['color'] and i != y:
                if colors[i]['matched'] is False and colors[y]['matched'] is False:
                    colors[i]['matched'] = True
                    colors[y]['matched'] = True
                    break

    # loop through the array to count the matched pairs and divided by two.
    for color in colors:
        if color['matched'] is True:
            counter += 1

    return int(counter / 2)


print(sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
