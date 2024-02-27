from canvas import Canvas
from PIL import Image


class Square:
    """Representatin of a square using it's upper left point and side length"""
    def __init__(self, x: int, y: int, side: int, color: list[str]):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
        
    def put_to_canvas(self, canvas: Canvas):
        canvas.pixel_array[self.x:self.side+self.x,  self.y:self.side+self.y] = self.color
        
        
def new_square() -> Square:
    upper_left_x = int(input("ENter upper left x: "))
    upper_left_y = int(input("ENter upper left y: "))
    
    side = int(input("Enter side of rectangle: "))

    red = int(input("How much red? "))
    green = int(input("How much green? "))
    blue = int(input("How much blue? "))
    
    return Square(upper_left_x, upper_left_y, side, [red, green, blue])