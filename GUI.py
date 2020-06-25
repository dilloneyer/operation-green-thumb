#########################################################################
########################## Loading Please Wait ##########################
######################### While We Import Things ########################
#########################################################################

#Importing tkinter, messages, <OTHER FILES IN MODULE HERE>
from tkinter import *
import tkinter.messagebox

#########################################################################
############################ Loading Complete ###########################
############################### Lets Begin ##############################
#########################################################################

# Class Initialization
class mainFrame:
    def __init__(self, frame):
        mainWidgetInit(frame)

class toolbarInit:
    def __init__(self, window):
        self.toolBar = Frame(window, bg="gainsboro")
        self.toolBar.pack(side=TOP, fill=X)

    def addBtn(self, btnName, frame):
        self.toolButton = Button(self.toolBar, text=btnName, command= lambda: mainSet(frame))
        self.toolButton.pack(side=LEFT, padx=2, pady=2)

def mainSet(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    mainWidgetInit(frame)

def btn1Set(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    testLabel = Label(frame, text="This is a test")
    testLabel.pack()
    print("Operations Menu")

def mainWidgetInit(frame):
    btnTopLeft = Button(frame, text="Operation", command= lambda: btn1Set(frame))
    btnTopLeft.grid(row=0, column=0)
    btnTopMid = Button(frame, text="Button 2")
    btnTopMid.grid(row=0, column=1)
    btnTopRight = Button(frame, text="Button 3")
    btnTopRight.grid(row=0, column=2)
    btnBotLeft = Button(frame, text="Button 4")
    btnBotLeft.grid(row=1, column=0)
    btnBotMid = Button(frame, text="Button 5")
    btnBotMid.grid(row=1, column=1)
    btnBotRight = Button(frame, text="Button 6")
    btnBotRight.grid(row=1, column=2)
    print("Main Menu")


# Application Runtime
window = Tk("Operation Green Thumb")
globalFrame = Frame(window, relief=SUNKEN)
toolBar = toolbarInit(window).addBtn("Home", globalFrame)
globalFrame.pack()

#window.attributes('-fullscreen', True) # **Note** Fullscreen command for windows
appInit = mainFrame(globalFrame)

window.mainloop()