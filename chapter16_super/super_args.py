class MyParentClass():
    def __init__(self, x, y):
        pass

class SubClass(MyParentClass):
    def __init__(self, x, y):
        super().__init__(x, y)