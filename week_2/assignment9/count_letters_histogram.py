from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

def show_result():
    analyze_file(filename.get())

def analyze_file(filename):
    try:
        inFile = open(filename, "r")

        # ... create a list counts ...
        counts = [0] * 26
        # ... for each line call count_letters ...
        for line in inFile:
            count_letters(line, counts)

        inFile.close()

        # show histogram
        histogram(counts)
    except IOError:
        tkinter.messagebox.showwarning("Analyze File",
                                    "File " + filename + " does not exist")
# count each letter in the string
def count_letters(line, counts):
    # ... for each char in line fill counts ...
    for char in line:
        charNum = (ord(char.lower()) - 97) # a = 0, z = 26
        if charNum < 26 and charNum > -1:
            counts[charNum] += 1


def open_file():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)

def histogram(counts):
    numberOfBars = len(counts)
    width = int(canvas["width"])
    height = int(canvas["height"])
    heightBar = 0.75 * height
    widthBar = width - 20
    maxCounts = max(counts)

    for i in range(numberOfBars):
        canvas.create_rectangle(i * widthBar / numberOfBars + 10, height - 20 - counts[i] * heightBar / maxCounts, (i + 1) * widthBar / numberOfBars + 10, height - 20)
        canvas.create_text(i * widthBar / numberOfBars + 10 + 0.5 * widthBar / numberOfBars, height - 10, text = chr(i + ord('a')))

window = Tk()
window.title("Occurrence of Letters Histogram")

frame1 = Frame(window) # frame for histogram
frame1.pack()
canvas = Canvas(frame1, width = 500, height = 200)
canvas.pack()

frame2 = Frame(window) # frame for buttons
frame2.pack()

Label(frame2, text = "Enter a filename: ").pack(side = LEFT)
filename = StringVar()
Entry(frame2, width = 40, textvariable = filename).pack(side = LEFT)
Button(frame2, text = "Browse", command = open_file).pack(side = LEFT)
Button(frame2, text = "Show Result", command = show_result).pack(side = LEFT)

window.mainloop()
