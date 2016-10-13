from tkinter import *
from random import randint
import time

class Plot:
    def __init__(self, s, x2, y2):
        self.s = s
        self.x2 = x2
        self.y2 = y2

    def step(self):
        if self.s == 23:
            # new frame
            self.s = 1
            self.x2 = 50
            canvas.delete('temp') # only delete items tagged as temp
        self.x1 = self.x2
        self.y1 = self.y2
        self.x2 = 50 + self.s * 50
        self.y2 = value_to_y(randint(0,100))
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='blue'\
        , tags='temp')
        
        self.s += 1
        canvas.after(300, self.step)

def value_to_y(val):
    return 550-5*val

# init global vars
s = 1
x2 = 50
y2 = value_to_y(randint(0,100))

objPlot = Plot(s, x2, y2)

# def step():
#     global s, x2, y2
#     if s == 23:
#         # new frame
#         s = 1
#         x2 = 50
#         canvas.delete('temp') # only delete items tagged as temp
#     x1 = x2
#     y1 = y2
#     x2 = 50 + s*50
#     y2 = value_to_y(randint(0,100))
#     canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
#     # print(s, x1, y1, x2, y2)
#     s = s+1
#     canvas.after(300, step)

root = Tk()
root.title('simple plot')

canvas = Canvas(root, width=1200, height=600, bg='white') # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)

Button(root, text='Quit', command=root.quit).pack()

canvas.create_line(50,550,1150,550, width=2) # x-axis
canvas.create_line(50,550,50,50, width=2)    # y-axis

# x-axis
for i in range(23):
    x = 50 + (i * 50)
    canvas.create_line(x,550,x,50, width=1, dash=(2,5))
    canvas.create_text(x,550, text='%d'% (10*i), anchor=N)

# y-axis
for i in range(11):
    y = 550 - (i * 50)
    canvas.create_line(50,y,1150,y, width=1, dash=(2,5))
    canvas.create_text(40,y, text='%d'% (10*i), anchor=E)

canvas.after(300, objPlot.step)
root.mainloop()
