class Vector:

    # Protected Static Class Variable:
    __staticVariable = 150

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    # Overloading the + operators for Vector objects:
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)