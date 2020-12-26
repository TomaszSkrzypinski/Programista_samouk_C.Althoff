class Rectangle:

    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def chang_size(self, w, l):
        self.width = w
        self.len = l


rectangle = Rectangle(10, 20)

print(rectangle.area())

rectangle.chang_size(20, 40)

print(rectangle.area())
