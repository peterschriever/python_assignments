global n
n = 5

def countdown():
    global n
    while n > 0:
        if n == 3:
            yield "spam"
        yield n
        n -= 2

for x in countdown():
    print(x)
    n += 1

# genObj = countdown()
# print(genObj)
# print([x for x in genObj])
