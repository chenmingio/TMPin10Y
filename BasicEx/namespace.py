x = 5
y = 6


def foo():
    x = 99
    print(x)
    y = 9999
    print(y)


print(foo.__dict__)
