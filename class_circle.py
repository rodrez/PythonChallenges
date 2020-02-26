class Circle():

    # Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * Circle.pi * 2

# Note: Notice how we have radius default to 1, we can pass a different number in the Circle
# class instantiation to change the default number of radius
my_circle = Circle()
print(my_circle.get_circumference())
print(my_circle.radius)
print(my_circle.pi)
