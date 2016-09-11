# Assignment 1.A
print("Assignment 1.A")
numericalList = [2, 3, 4]
print(numericalList)

print("\n")

# Assignment 1.B
print("Assignment 1.B")
wordList = ["red", "green", "blue"]
print(wordList)

print("\n")

# Assignment 1.C
print("Assignment 1.C")
numericalListUsingRange = list(range(3, 6))
print(numericalListUsingRange)

print("\n")

# Asssignment 1.D
print("Assignment 1.D")
characterList = ['a', 'b', 'c', 'd']
print(characterList);

print("\n")

# Assignment 2 A - M
print("Assignment 2 A - M")
L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
print("a: "+str(L.index(1))) # A

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
print("b: "+str(L.count(1))) # B

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
print("c: "+str(len(L))) # C

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
#print("d: "+str(max(L))) # D
# The max() function raises a TypeError in python3.5
# Ref: http://stackoverflow.com/questions/34795757/using-max-on-a-list-containing-strings-and-integers

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
L.append(40) # The append function itself simply returns None
print("e: "+str(L)) # E

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
L.insert(1, 43) # The insert function simply returns None
print("f: "+str(L)) # F

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
L.extend([1,43]) # The extend function simply returns None
print("g: "+str(L)) # G

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
L.remove("hello") # The remove function simply returns None
print("h: "+str(L)) # H

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
print("i: "+str(L.pop())) # I

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
print("j: "+str("Goodbye" in L)) # J

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
print("k: "+str(L.pop(3))) # K

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
#print("l: "+str(L.sort())) # L
# Brings out the same TypeError as the max() function in 2.D

L = [30, 1, 2, 1, 0, "hello", "Goodbye"]
import random
random.shuffle(L) # The random.shuffle() function simply returns None
print("m: "+str(L)) # M

print("\n")

# Assignment 3
print("Assignment 3 A - D")

L = [2, 3, 5, 2, 33, 21]
# Slice the list: From the index: 1 until len(L)-3
# if either number is negative, the index is relative to the end of the string
# len(s) + i or len(s) + j
# Ref: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
# See note 3.
print("a: "+str(L[1 : -3])) # a

L = [2, 3, 5, 2, 33, 21]
print("b: "+str(L[-4 : -2])) # b

L = [2, 3, 5, 2, 33, 21]
# Don't do this at home! Results in the same as simply calling L
# Lol.
print("c: "+str(L[:2] + L[2:])) # c

L = [2, 3, 5, 2, 33, 21]
print("d: "+str(L[42:])) # d

print("\n")

# Assignment 4
print("Assignment 4 A - E")

L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]
print("a: "+str(L1 + L2)) # a

L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]
print("b: "+str(3*L2)) # b

L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]
print("c: "+str(L1 > L2)) # c

L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]
print("d: "+str([x for x in L1]))

L1 = [30, 1, 2, 1, 0]
L2 = [1, 21, 13]
# TODO: unexpected EOF while parsing
#print("e: "+str([x for x in L1 if x in L1]) # e

print("\n")

# Assignment 5
print("Assignment 5")
s = "Guido van Rossum"
L = s.split(' ')
print(L)

print("\n")

# Assignment 6
print("Assignment 6 A - C")

print("Start a")
# note to self: don't do this.
# Use descriptive variable names!
# Code should be easy to read!
L = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    L[i] = L[i - 1]
    print(L)
print("End a")

print("Start b")
L1 = list(range(1, 10, 2))
L2 = L1
L1[0] = 111 # remember: because L2 = L1, if we change L1 the same happens to L2
print(L1)
print(L2)
print("End b")

print("Start c")
a, b = 0, 1 # pls don't do this a = 0, b = 1
while b < 10:
    print (b)
    # a = b, b = a+b !== b = b+b
    # Because a = b happens at the same time as b = a+b.
    # So eg: a = 0, b = 1
    # a(0) = 1(b), b(1) = 0(a)+1(b) => a(1) = 1(b), b(1) = 1(a)+1(b)
    # This explains the double 1 and skips in numbers.
    # But honestly, I feel like this is some pretty bad code..
    a, b = b, a+b
print("End c")

print("\n")

# Assignment 7
print("Assignment 7 A Tuple vs List")

aTuple = 123, 555, "Foo Bar!", 'a'
aList = [123, 555, "Foo Bar!", 'a']
print(aTuple)
print(aList)

# Both may be nested
anotherTuple = 111, 222, aTuple
print(anotherTuple)
anotherList = [111, 222, aList]
print(anotherList)

# Tuples are immutable / their values can not be changed
#aTuple[0] = "This will throw an error."

print("\n")

print("Assignment 7 B")
aTuple = 123, 321, "bar"
aList = [222, 'm', "zzz"]
tupleToList = list(aTuple)
listToTuple = tuple(aList)
print("aTuple converted to a List: " + str(tupleToList))
print("aList converted to a Tuple: " + str(listToTuple))

print("\n")

print("Assignment 7 C - E")
# c
t = (1, 2, 3)
#t.append(4) # no attribute 'apend'
#t.remove(0) # no attribute 'remove'
#t[0] = 1 # tuple is immutable

# d
y = 9
x = y**0,5 # The comma is actually making a tuple here
#z = 10 - x # TypeError because you can not subtract an integer from a tuple

# e
b = ("Bob", 19, "CS")
(x, y, z) = b # unpacking
print ('age = ',y) # Note to self: comma allows you to print stuff in sequence or something like that.

print("\n")

# Assignment 
