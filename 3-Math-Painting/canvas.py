import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width: int, height: int, color: str):
        self.width = width
        self.height = height
        self.color = color
        
        # Instantiate the pixel array
        self.pixel_array = np.zeros((height, width, 3), dtype=np.uint8)
        self.pixel_array[:] = [255, 255, 255] if color == "white" else [0, 0, 0]
        
        
    def output(self):
        img = Image.fromarray(self.pixel_array, "RGB")
        img.save("output.png")
        
def new_canvas() -> Canvas:
    width = int(input("Enter canvas width: "))
    height = int(input("Enter canvas height: "))
    color = input("Enter canvas color (black or white): ")
    return Canvas(width, height, color)