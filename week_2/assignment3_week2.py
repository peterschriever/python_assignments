import collections

# Assignment 3.A
d = {'red':'#FF0000', 'green':'#008000', 'black':'#000000', 'white':'#FFFFFF'}
od = collections.OrderedDict(sorted(d.items()))
print("d: ", d)
print("od: ", od)
print(od['green'])

# Assignment 3.B
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

print("Assignment 3.B")
print("Expected result: ", {'x': 300, 'y': 200, 'a': 100, 'b': 200})
d1.update(d2)
print("Actual result: ", d1)
