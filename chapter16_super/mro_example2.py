class Base:
    var = 5
    def __init__(self):
        pass

class X(Base):
    def __init__(self):
        print('X')
        super().__init__()

class Y(Base):
    var = 10
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X, Y):
    pass


z = Z()
print(Z.__mro__)
print(super(Z, z).var)