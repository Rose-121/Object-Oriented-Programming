class Circle:
    def __init__(self, r):
       
        self.radius = r

    def area(self):
        
        return 3.1416 * (self.radius ** 2)

    def perimeter(self):
        
        return 2 * 3.1416 * self.radius


radius = float(input("Enter the Radius: "))


c1 = Circle(radius)


print(f"Area: {c1.area()}")
print(f"Perimeter: {c1.perimeter()}")