from canvas import Canvas


class Rectangle:
    """Representation of a rectangle using upper left point and it's lengths"""
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color= color
        
    def put_to_canvas(self, canvas: Canvas):
        canvas.pixel_array[self.x:self.height+self.x,  self.y:self.width+self.y] = self.color
        
def new_rectangle() -> Rectangle:
    upper_left_x = int(input("ENter upper left x: "))
    upper_left_y = int(input("ENter upper left y: "))
    
    width = int(input("Enter width of rectangle: "))
    height = int(input("Enter height of rectangle: "))
    
    red = int(input("How much red? "))
    green = int(input("How much green? "))
    blue = int(input("How much blue? "))
    
    return Rectangle(upper_left_x, upper_left_y, width, height, [red, green, blue])