class MyParentClass(object):
    def __init__(self):
        pass

class SubClass(MyParentClass):
    def __init__(self):
        MyParentClass.__init__(self)