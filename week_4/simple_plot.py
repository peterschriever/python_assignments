from tkinter import *
from random import randint
import time

def makeTkEntry(parent, label, width=None, **options):
    Label(parent, text=label).pack()
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack()
    return entry

def value_to_y(val):
    return 550-5*val


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
        _plottingPaused (bool): Pause the plotting process when True
        pauseInMs (int): Amount in milliseconds to wait before drawing again
        btnPause (Button): Gui button which is used to toggle the plotting state
        txtMaxY (TextField): Gui textfield which contains the max-y value
        txtMinY (TextField): Gui textfield which contains the min-y value
        yMinValue (int): The current minimal value for the Y-axis
        yMaxValue (int): The current maximal value for the Y-axis
    """

    _PLOT_STEP_BOUNDARY = 23

    def __init__(self, s, x2, y2, pauseInMs):
        self._plottingPaused = False
        self.s = s
        self.x2 = x2
        self.y2 = y2
        self.pauseInMs = pauseInMs
        self.yMinValue = 0
        self.yMaxValue = 100

    def drawGuiWithTk(self):
        self.guiRoot = Tk() # guiRoot element is to place tkinter widgets on
        self.guiRoot.title('simple plot')
        self.guiControlsFrame = Frame(self.guiRoot, width=200, borderwidth=5)
        self.guiControlsFrame.pack(side=RIGHT, fill=Y, expand=1)
        self.addGuiButtons()
        self.addGuiConfigFields()
        self.initializeCanvas()
        self.drawCanvasAxes()
        self.addCanvasLabels()

    def addGuiConfigFields(self):
        self.txtMinY = makeTkEntry(self.guiControlsFrame, "Min-y: ", 10)
        self.txtMinY.insert(0, '0')
        self.txtMaxY = makeTkEntry(self.guiControlsFrame, "Max-y: ", 10)
        self.txtMaxY.insert(0, '100')
        self.btnSetMaxMin = Button(self.guiControlsFrame, text="Set",
            command=self.setNewMinMax)
        self.btnSetMaxMin.pack()

    def setNewMinMax(self):
        newMinY = int(self.txtMinY.get())
        newMaxY = int(self.txtMaxY.get())
        if newMinY >= 0 and newMinY <= 100 and \
        newMaxY >= newMinY and newMaxY <= 100:
            self.yMinValue = newMinY
            self.yMaxValue = newMaxY
            self.canvas.delete('minMaxY') # remove old Y-limit lines
            self.drawNewMinMaxLine(newMinY)
            self.drawNewMinMaxLine(newMaxY)
        else:
            print("Error: new min/max Y are incorrect: ", newMinY, newMaxY)

    def drawNewMinMaxLine(self, newY):
        self.canvas.create_line(50,value_to_y(newY),1150,value_to_y(newY),
            width=3, tags='minMaxY')

    def addCanvasLabels(self):
        lblOptions = {"bg": "white", "fg": "black"}
        lblValue = Label(self.guiRoot, text="Value", wraplength=1, **lblOptions)
        lblStep = Label(self.guiRoot, text="Step", **lblOptions)
        self.canvas.create_window(20, 275, window=lblValue)
        self.canvas.create_window(100, 20, window=lblStep)

    def initializeCanvas(self):
        # 0,0 is top left corner
        self.canvas = Canvas(self.guiRoot, width=1200, height=600, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

    def drawCanvasAxes(self):
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
        Button(self.guiControlsFrame, text='Quit',
            command=self.guiRoot.quit).pack()

        self.btnPause = Button(self.guiControlsFrame, text="Pause",
            command=self.togglePlotting)
        self.btnPause.pack()

    def togglePlotting(self):
        if self._plottingPaused: # current state is paused
            self.keepPlotting()
            self.btnPause.config(text="Pause")
            self._plottingPaused = False
        else: # current state is running
            self.canvas.after_cancel(self.canvasCmdAfterId) # cancel queued cmd
            self.btnPause.config(text="Continue")
            self._plottingPaused = True

    def plotOneStep(self):
        if self.s == self._PLOT_STEP_BOUNDARY:
            # step limit reached; draw a new plot
            self.s = 1
            self.x2 = 50
            self.canvas.delete('temp') # only delete items tagged as temp

        x1 = self.x2
        y1 = self.y2
        self.x2 = 50 + self.s * 50
        self.y2 = value_to_y(randint(self.yMinValue, self.yMaxValue))
        self.canvas.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')
        self.s = self.s + 1

    def keepPlotting(self):
        self.plotOneStep()
        self.canvasCmdAfterId = self.canvas.after(self.pauseInMs, self.keepPlotting)

# init vars
s = 1
x2 = 50
y2 = value_to_y(randint(0,100))

# Create the Plot instance
objPlot = Plot(s, x2, y2, 300)
objPlot.drawGuiWithTk()
objPlot.keepPlotting()
objPlot.guiRoot.mainloop() # start Tkinter event loop.
# Tkinter event loop: http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm
