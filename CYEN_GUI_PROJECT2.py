from tkinter import *
import text

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

def process0():
    print("hello")
def process1():
    print("myname is")
    pass
def process2():
    pass
def process3():
    pass
def process4():
    pass
def process5():
    pass
def process6():
    pass
def process7():
    pass
def process8():
    pass


f1 = Frame(window)
f2 = Frame(window)
l1 = Label(f1, text="MARBLE MAZE", font=("Courier",30))
l1.grid(row=0,column=1,sticky=N+S+E+W)
infoB = Button(f1,text="Info",font=("Courier",10),command=switch)
infoB.grid(row=1,column=1,sticky=N+S+E+W)
backB = Button(f2,text="Back",font=("Courier",10),command=switchBack)
backB.grid(row=0,column=1,sticky=N+S+E+W)
t1 = text.text_window(f2)

a=0
for row in range(len(buttonDisplays)):
    for column in range(len(buttonDisplays[row])):
        img = PhotoImage(file=folder+buttonDisplays[row][column]+".png")
        process = [process0,process1,process2,process3,process4,process5,process6,process7,process8]
        button = Button(f1, bg="white", image=img, borderwidth=0, highlightthickness=0,activebackground="white", command=process[a])
        button.image = img
        button.grid(row=row+2, column=column, sticky=N+S+E+W)
        a+=1



window.title("CYEN Marble Maze 1.0")
f1.pack()
window.mainloop()




