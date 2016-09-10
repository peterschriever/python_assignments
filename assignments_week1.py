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
