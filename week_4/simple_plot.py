from tkinter import *
from random import randint
import time

class Plot:
    """ The Plot class which draws and manages a simple tkinter plot

    Class Fields:
        s (int): The step counter, remember which step we are on.
        x2 (int): The initial x-axis value to start drawing from.
        y2 (int): The initial y-axis value to start drawing from.
        guiRoot (:obj: `Tk`): The root GUI element to place tkinter widgets on
        canvas (:obj: `Canvas`): The canvas used to plot a graph
        _PLOT_STEP_BOUNDARY (int):  The boundary at which a new frame
                                    has to be drawn

    """

    _PLOT_STEP_BOUNDARY = 23

    def __init__(self, s, x2, y2):
        self.s = s
        self.x2 = x2
        self.y2 = y2

    def drawGuiWithTk(self):
        self.guiRoot = Tk() # guiRoot element is to place tkinter widgets on
        self.guiRoot.title('simple plot')
        self.initializeCanvas()
        self.addGuiButtons()

    def initializeCanvas(self):
        # 0,0 is top left corner
        self.canvas = Canvas(self.guiRoot, width=1200, height=600, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

        self.canvas.create_line(50,550,1150,550, width=2) # draw x-axis
        self.canvas.create_line(50,550,50,50, width=2)    # draw y-axis

        # fill axis-steps
        for i in range(23):
            x = 50 + (i * 50)
            self.canvas.create_line(x,550,x,50, width=1, dash=(2,5))
            self.canvas.create_text(x,550, text='%d'% (10*i), anchor=N)
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50,y,1150,y, width=1, dash=(2,5))
            self.canvas.create_text(40,y, text='%d'% (10*i), anchor=E)

    def addGuiButtons(self):
        Button(self.guiRoot, text='Quit', command=self.guiRoot.quit).pack()

    def plotOneStep(self):
        if self.s == self._PLOT_STEP_BOUNDARY:
            # draw a new frame
            self.s = 1
            self.x2 = 50
            self.canvas.delete('temp') # only delete items tagged as temp

        x1 = self.x2
        y1 = self.y2
        self.x2 = 50 + self.s * 50
        self.y2 = value_to_y(randint(0,100))
        self.canvas.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')
        self.s = self.s + 1

    def keepPlottingEvery(self, pauseInMs):
        self.plotOneStep()
        self.canvas.after(pauseInMs, self.keepPlottingEvery, pauseInMs)


def value_to_y(val):
    return 550-5*val

# init global vars
s = 1
x2 = 50
y2 = value_to_y(randint(0,100))

# Create the Plot instance
objPlot = Plot(s, x2, y2)
objPlot.drawGuiWithTk()
objPlot.keepPlottingEvery(300)
objPlot.guiRoot.mainloop() # start Tkinter event loop.
# Tkinter event loop: http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm
