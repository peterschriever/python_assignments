# Assignment 2
d = {"red":4, "blue":1, "green":14, "yellow":2}
print("Initial state: ", d)
d['red'] = d['blue']
print("a: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d['blue'] += 10
print("b: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d['yellow'] = len(d)
print("c: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d['green'] = {'orange' : 6}
print("d: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d = dict(zip(d.keys(), d.values()))
print("e: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d = dict.fromkeys(d, 0)
print("f: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d.pop('black', None)
print("g: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d.get('black', None)
print("h: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d.setdefault('black', None)
print("i: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d = {k : 0 for k in d.keys()}
print("j: ", d)

d = {"red":4, "blue":1, "green":14, "yellow":2}
d = {}
print("k: ", d)
