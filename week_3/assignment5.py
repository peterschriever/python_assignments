try:
    lst = 10 * [0]
    x = lst[10]
    print("Done ")

except IndexError:
    print("Index out of bound")

else:
    print("Nothing is wrong")

finally:
    print("Finally we are here")

print("Continue")
