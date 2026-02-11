class Obj:
    def __init__(self):
        pass

a = Obj()
b = a
del b
print(a)
print(b)