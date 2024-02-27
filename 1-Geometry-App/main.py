from math import pow
from math import sqrt
from random import randint
import turtle


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt(pow((self.x - other.x, 2)) + pow(self.y - other.y, 2))

    def included_by(self, rect):
        x_check = rect.lower_left.x < self.x < rect.upper_right.x

        y_check = rect.lower_left.y < self.y < rect.upper_right.y
        return x_check and y_check


class Rectangle:
    def __init__(self, lower_left: Point, upper_right: Point):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def width(self) -> float:
        return self.upper_right.x - self.lower_left.x

    def height(self) -> float:
        return self.upper_right.y - self.lower_left.y

    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return 2 * (self.width() + self.height())

    def introduce(self):
        return (f"lower left point: {(self.lower_left.x, self.lower_left.y)}\n" +
                f"upper right point: {(self.upper_right.x, self.upper_right.y)}")



class GuiRectangle(Rectangle):
    def __init__(self, lower_left: Point, upper_right: Point):
        super().__init__(lower_left, upper_right)

    def draw_rectangle(self, canvas):
        canvas.penup()
        canvas.goto(self.lower_left.x, self.lower_left.y)
        canvas.pendown()

        width = self.width()
        height = self.height()

        canvas.forward(width)
        canvas.left(90)
        canvas.forward(height)
        canvas.left(90)
        canvas.forward(width)
        canvas.left(90)
        canvas.forward(height)


def new_random_rectangle() -> GuiRectangle:
    lower_left = Point(randint(-100, 100), randint(-100, 100))
    upper_right = Point(randint(100, 200), randint(100, 200))
    return GuiRectangle(lower_left, upper_right)


class GuiPoint(Point):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    def draw_point(self, canvas, size=5, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


def get_user_point():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    return GuiPoint(x, y)


def main():
    print("welcome to the game.\n"
          "you should guess one point inside of a random generated rectangle.\n"
          "------------------------------------------------------------------")

    rect = new_random_rectangle()
    print(rect.introduce())

    user_point = get_user_point()
    print("you guessed right") if user_point.included_by(rect) else print("Oops!! wrong guess")

    user_area_guess = float(input("Guess the area of rectangle: "))
    print("you guessed right") if user_area_guess == rect.area() else print("Oops!! wrong guess")

    my_turtle = turtle.Turtle()

    rect.draw_rectangle(my_turtle)
    user_point.draw_point(my_turtle)

    turtle.done()


if __name__ == "__main__":
    main()
