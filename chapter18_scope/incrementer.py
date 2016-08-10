def counter():
    num = 0
    def incrementer():
        num += 1
        return num
    return incrementer