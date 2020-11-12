class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for h in range(self.height):
                picture += "*" * self.width + "\n"
            return picture

    def get_amount_inside(self, shape):
        count = 0
        if self.get_perimeter() > shape.get_perimeter():
            for h in range(self.height, shape.height - 1, -shape.height):
                for w in range(self.width, shape.width - 1, -shape.width):
                    count += 1
        return count

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side
        self.width = side
        self.height = side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return "Square(side={})".format(self.side)

