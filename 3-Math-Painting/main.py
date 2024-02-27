from canvas import new_canvas
from square import  new_square
from rectangle import new_rectangle


def main():
    canvas = new_canvas()
    
    while True:
        shape = input("Set the shape you want to draw(rectangle or square): ").strip().lower()
        
        if shape == "rectangle":
            rectangle = new_rectangle()
            rectangle.put_to_canvas(canvas)
        elif shape == "square":
            square = new_square()
            square.put_to_canvas(canvas)
        
        keep_running = input("Press enter to continue. press o to get output: ")
        if keep_running == "o":
            break
        
    canvas.output()
        
    
    
if __name__ == '__main__':
    main()
        
    