class A:
    def show(self):
        print("A's show()")

class B(A):
    def show(self):
        print("B's show()")

class C(A):
    def show(self):
        print("C's show()")

class D(B, C):
    pass

# Usage
d = D()
d.show()
print(D.__mro__)  # Shows the method resolution order
