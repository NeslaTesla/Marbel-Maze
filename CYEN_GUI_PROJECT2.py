from tkinter import *

buttonDisplays = [
    ["LUDia","Up","RUDia"],
    ["Left","Center","Right"],
    ["LDDia","Down","RDDia"]
]

folder = "CYEN_images/"
buttonDef = {
    "info": "[]",
    "LUDia": "^<-",
    "Up": "^^",
    "RUDia": "->^",
    "Left": "<-",
    "Center": "0",
    "Right": "->",
    "LDDia": "d<-",
    "Down": "D",
    "RDDia": "->d"
}
window = Tk()

def switch():
    f2.pack()
    f1.forget()

def switchBack():
    f1.pack()
    f2.forget()

def process():
    pass

f1 = Frame(window)
f2 = Frame(window)
l1 = Label(f1, text="MARBLE MAZE", font=("TexGyreAdventure",20))
l1.grid(row=0,column=1,sticky=N+S+E+W)
infoB = Button(f1,text="info",font=("TexGyreAdventure",10),command=switch)
infoB.grid(row=1,column=1,sticky=N+S+E+W)
backB = Button(f2,text="back",font=("TexGyreAdventure",10),command=switchBack)
backB.grid(row=0,column=1,sticky=N+S+E+W)

for row in range(len(buttonDisplays)):
    for column in range(len(buttonDisplays[row])):
        img = PhotoImage(file=folder+buttonDisplays[row][column]+".png")
        button = Button(f1, bg="white", image=img, borderwidth=0, highlightthickness=0,activebackground="white", command=process)
        button.image = img
        button.grid(row=row+2, column=column, sticky=N+S+E+W)
# LUimg = PhotoImage(file=folder+"LUDia.gif")
# LU = Button(f1,image=LUimg,borderwidth=0,highlightthickness=0,activebackground="white",command=process)
# LU.grid
# LU.image = LUimg



window.title("CYEN Marble Maze 1.0")
f1.pack()
window.mainloop()


