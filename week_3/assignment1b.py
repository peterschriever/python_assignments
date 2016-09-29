class A:
    def __init__(self, i):
        self.i = i
    def __str__(self):
        return "I am class A"

class B(A):
    def __init__(self, i, j):
        super().__init__(i)
        self.j = j
    def __str__(self):
        return "I am class B"

def main():
    a = A(1)
    b = B(1, 2)
    print(a)
    print(b)
    print(a.__dict__)
    print(b.__dict__)

main()
