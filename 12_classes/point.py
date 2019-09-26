class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"drawing point at x={self.x}, y={self.y}")

    def move(self):
        print("move")


point1 = Point(x=10, y=20)
point1.draw()
