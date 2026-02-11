import weakref
class Obj:
    def __init__(self):
        self.next = None

a = Obj()
b = Obj()
c = Obj()
w = weakref.ref(b)
a.next = b
b.next = c
del b
print(w())

a.next = c
print(w())
