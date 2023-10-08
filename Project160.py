from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import os, webbrowser

root = Tk()
root.title('HTML IDE')
root.minsize(650, 650)
root.configure(background = 'snow')

def getImg(imgName):
    return ImageTk.PhotoImage(Image.open(imgName))

imgs = []
for i in range(3):
    imgs.append(getImg(f'Project160+/Icons/Icon { i }.png'))

lblFileName = Label(root, text = 'File Name:', bg = 'light blue', fg = 'black')
lblFileName.place(relx = 0.3, rely = 0.05, anchor = CENTER)

entFileName = Entry(root)
entFileName.place(relx = 0.5, rely = 0.05, anchor = CENTER)

myTxt = Text(root, width = 70, height = 35)
myTxt.place(relx = 0.5, rely = 0.1, anchor = N)

name0 = ''

def openFile():
    global name0
    myTxt.delete(1.0, END)
    entFileName.delete(0, END)
    name0 = filedialog.askopenfilename(
    title = 'Open HTML Files', 
    filetypes = (('HTML Files', '*.html'),)
    )
    name1 = os.path.basename(name0)
    name2 = name1.split('.')[0]
    entFileName.insert(END, name2)
    name2 = open('Project160+/Websites/' + name1, 'r')
    paragraph = name2.read()
    myTxt.insert(END, paragraph)

def saveFile():
    name = entFileName.get()
    FILE = open(f'Project160+/Websites/{ name }.html', 'w')
    data = myTxt.get(1.0, END)
    print(data)
    FILE.write(data)
    messagebox.showinfo('Info', 'Saved Successfully')

def runFile():
    global name0
    webbrowser.open(name0)

btnOpenFile = Button(root, image = imgs[0], command = lambda: openFile())
btnOpenFile.place(relx = 0.1, rely = 0.05, anchor = CENTER)
btnSaveFile = Button(root, image = imgs[1], command = lambda: saveFile())
btnSaveFile.place(relx = 0.15, rely = 0.05, anchor = CENTER)
btnRunFile = Button(root, image = imgs[2], command = lambda: runFile())
btnRunFile.place(relx = 0.2, rely = 0.05, anchor = CENTER)

root.mainloop()