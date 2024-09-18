class recgtangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
       return self.width*self.height
    def perimeter(self):
       return 2*self.width+self.height

rect=recgtangle(4,5)
print(f"area: {rect.area()}")
print(f"perimeter: {rect.perimeter()}")
        