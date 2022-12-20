#Create class
class Rectangle:
    #create init method
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2*(self.length+self.width)

    def Area(self):
        return self.length*self.width

    def Display(self):
        print('length is:', self.length)
        print('width is:', self.width)
        print('perimeter is:', self.Perimeter())
        print('Area is:', self.Area())


# Create new class that inheretis the Rectangle class

class Cube (Rectangle):
    def __init__(self, length, width, height):
        #super().__init__(length, width)
        Rectangle.__init__(self, length, width)
        self.height=height
    
    def Volume(self):
        return self.length*self.height*self.width

#create instance of class; you can create multiple instances from the class
myRectangle = Rectangle(3,2)
# Instance can access all methods in the class
myRectangle.Display()
print("-------------------------------------------------------------")
myRectangle2 = Rectangle(5, 6)
myRectangle2.Display()
print("-------------------------------------------------------------")

myCube= Cube(2,3,4)
print("Cube Volume is :", myCube.Volume())
