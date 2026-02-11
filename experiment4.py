class Obj:
    def __init__(self, x):
        self.x = x

a = Obj(5)
del a.x
print(a)
print(a.x)