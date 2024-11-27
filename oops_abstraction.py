from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
rectange=Rectangle(10,5)
print("rectangle area:",rectange.area())