def my_func(a, b):
    global c
    # swap a and b
    b, a = a, b
    d = 'Mike'
    print(a, b, c, d)

a, b, c, d = 1, 2, 'c is global', 4
my_func(1, 2)
print(a, b, c, d)