###### credit to Yochai ######


def add(x, y):
    if y == 0:
        return x
    else:
        return 1 + add(x, y-1)


def mul(x, y):
    if y == 1:
        return x
    else:
        return add(x, mul(x, y-1))


def fuct(x):
    if x == 0:
        return 1
    else:
        return mul(fuct(x-1), x)


