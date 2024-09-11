*Class 2: Rectangle*


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Usage
rectangle = Rectangle(5, 4)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
```