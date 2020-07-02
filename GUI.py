#########################################################################
########################## Loading Please Wait ##########################
######################### While We Import Things ########################
#########################################################################

#Importing tkinter, messages, pillow, <OTHER FILES IN MODULE HERE>
from tkinter import *
from PIL import ImageTk, Image
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

    def addBtn(self, frame):
        homePhoto = photoInit("home.png", 25, 25)
        self.toolHome = Button(self.toolBar, image=homePhoto, command= lambda: mainSet(frame))
        self.toolHome.pack(side=LEFT, padx=2, pady=2)
        self.toolHome.image = homePhoto
        settingPhoto = photoInit("settings.png", 25, 25)
        self.toolSetting = Button(self.toolBar, image = settingPhoto)
        self.toolSetting.image = settingPhoto
        self.toolSetting.pack(side=LEFT, padx=2, pady=2)

def photoInit(fileName, sizex, sizey):
        rawPhoto = Image.open(fileName)
        rsizePhoto = rawPhoto.resize((sizex, sizey), Image.ANTIALIAS)
        newPhoto = ImageTk.PhotoImage(rsizePhoto)
        return newPhoto

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
    btnTopLeft.grid(row=0, column=0, padx=5, pady=(150, 5))
    btnTopMid = Button(frame, text="Monitor")
    btnTopMid.grid(row=0, column=1, padx=5, pady=(150, 5))
    btnTopRight = Button(frame, text="Button 3")
    btnTopRight.grid(row=0, column=2, padx=5, pady=(150, 5))
    btnBotLeft = Button(frame, text="Button 4")
    btnBotLeft.grid(row=1, column=0)
    btnBotMid = Button(frame, text="Button 5")
    btnBotMid.grid(row=1, column=1)
    btnBotRight = Button(frame, text="Button 6")
    btnBotRight.grid(row=1, column=2)
    print("Main Menu")


# Application Runtime
window = Tk()
window.geometry("800x600")
window.title("Operation Green Thumb")
globalFrame = Frame(window, relief=SUNKEN)
toolBar = toolbarInit(window).addBtn(globalFrame)

globalFrame.pack()

#window.attributes('-fullscreen', True) # **Note** Fullscreen command for windows
appInit = mainFrame(globalFrame)

window.mainloop()
