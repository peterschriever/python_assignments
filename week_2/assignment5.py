# Assignment 5.A
# print("5.A: ")
# def function1(n, m):
#     function2(3.4)
#
# function1(2, 3)
#
# def function2(n):
#     if n > 0:
#         return 1
#     elif n == 0:
#         return 0
#     elif n < 0:
#         return -1
# print("\n")

print("5.B: ")
def main():
    print(min('Jan', 'jan'))

def min(n1, n2):
    smallest = n1
    if n2 < smallest:
        smallest = n2

main()
print("\n")

print("5.C: ")
def intersect(seq1, seq2):
    res = set()
    for x in seq1:
        if x in seq2:
            res.add(x)
    return res # seq1 & seq2

print(intersect('beer', 'burger'))
print(intersect((1,2,3,4),(1,4,2,5)))
print(intersect({1,2,3,4},{1,4,2,5}))
print("Pythonic?: ", set('beer') & set('burger'))
print("\n")

print("5.D: ")
v = 42

def do():
    v = 0
    v += 1
    print(v) # v exists in local scope, print that version

def da():
    global v # out of scope v was read and made global
    v += 1
    print(v)

do()
da()
print(v)
print("\n")

print("5.E: ")
def make(N):
    return lambda x: x**N

square = make(2)
cube = make(3)
hyper = make(4)

print(square(3)) # 3^2 == 3**2
print(cube(3)) # 3^3 == 27
print(hyper(3)) # 3^4 == 81
print("\n")
