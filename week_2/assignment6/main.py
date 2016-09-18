#main.py
from moda import Simple # Import statement does not include the Simple class.
from modb import *
from modc import x,y

f1('hi')
f2()
print(y)


z=Simple() # Throws an error because Simple class does not exist
z.display()
