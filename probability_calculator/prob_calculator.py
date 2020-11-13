import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)

    def draw(self, num):
        contents = self.contents
        if num >= len(self.contents):
            return contents
        else:
            draw_list = []
            for x in range(num):
                choice = random.choice(contents)
                contents.remove(choice)
                draw_list.append(choice)
            self.contents = contents
            return draw_list


def check(expected, draw):
    """
    Checks if the expected in the draw.
    :param expected: list of expected balls.
    :param draw: current draw from contents
    :return: bool
    """
    for color in expected:
        if color in draw:
            draw.remove(color)
            continue
        else:
            return False
    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected = []
    M = 0
    for color, count in expected_balls.items():
        for i in range(count):
            expected.append(color)

    for n in range(num_experiments):
        chance = copy.deepcopy(hat)
        draw = chance.draw(num_balls_drawn)

        result = check(expected, draw)
        if result:
            M += 1
    probability = M / num_experiments
    return probability


h = Hat(red=3, yellow=2, blue=2, green=2)
# print("draw ", hat.draw(4), "contents", hat.contents)
experiment(hat=h, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=1000)
