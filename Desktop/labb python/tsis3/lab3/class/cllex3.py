class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


rectangle = Rectangle(4, 5)
print("Area of rectangle with length 4 and width 5:", rectangle.area())
