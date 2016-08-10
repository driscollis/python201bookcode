class X:
    def __init__(self):
        print('X')
        super().__init__()

class Y:
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)