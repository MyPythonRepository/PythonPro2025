class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.radius ** 2


circle = Circle(0, 0, 10)
point1 = Point(5, 8)
point2 = Point(11, 18)

print(circle.contains(point1))
print(circle.contains(point2))
