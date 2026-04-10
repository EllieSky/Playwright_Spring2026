class A:
    def __init__(self, first):
        self.first = first

class B(A):
    def __init__(self, first, second):
        super().__init__(first)
        self.second = second

class C(B):
    def __init__(self, first = None, second = None, third = None):
        if isinstance(first, B):
            b_obj = first
            first = b_obj.first
            second = b_obj.second
        super().__init__(first, second)
        self.third = third


c1 = C("1", "2", "3")


c2 = C(B("5", "6"), third="7")
c2_2 = C(second = B("5", "6"))   # Not intentional

c3 = C("4")  # Not intentional

# --------------------------------------------------

class DrawShape:
    def __init__(self, shape: Shape):
        self.shape = shape

    def draw(self):
        # self.shape.draw()
        print(f"Drawing a {self.shape.color} {self.shape.type}")


class Shape:
    def __init__(self, color):
        self.color = color

class Triangle(Shape):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'triangle'

class Square(Shape):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'square'

class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'circle'

shape1 = DrawShape(Triangle("blue"))

shape2 = DrawShape(Circle("red"))

shape3 = DrawShape(Square("yellow"))

shape3.draw()
shape2.draw()
shape1.draw()


