def outer():
    x = 1
    def inner():
        return x
    print(inner())
    return


def outer2():
    def inner2():
        return x
    x = 1
    print(inner2())
    return
