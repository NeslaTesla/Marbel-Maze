from tkinter import *
import text
import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(12,GPIO.IN)
GPIO.setup(27,GPIO.IN)
GPIO.setup(23,GPIO.IN)
GPIO.setup(21,GPIO.IN)
GPIO.setup(25,GPIO.IN)
#17,12,27,23,21,25
# outputs LED and possibly speaker
path1= [17,12]
end1=27
path2=[21,25]
end2=23

paths=[path1,path2]
def new_path(paths):
    return paths[randint(0,1)]
correctpath = new_path(paths)
if 17 in correctpath:
    correctend = end1
else:
    correctend = end2
correctpath.append(correctend)
ballmotion = []

window = Tk()

def switch():
    f2.pack()
    f1.forget()

def switchBack():
    f1.pack()
    f2.forget()

def reset():
    ballmotion.clear()
    x = new_path(paths)
    correctpath = x


HEIGHT = 600

f1 = Frame(window)
f2 = Frame(window)
l1 = Label(f1, text="MARBLE MAZE", font=("Courier",30))
l1.grid(row=0,column=1,sticky=N+S+E+W)
infoB = Button(f1,text="Info",font=("Courier",10),command=switch)
infoB.grid(row=1,column=1,sticky=N+S+E+W)
backB = Button(f2,text="Back",font=("Courier",10),command=switchBack)
backB.grid(row=0,column=1,sticky=N+S+E+W)
resetB = Button(f1,text="Reset",font=("Courier",10),command=reset)
resetB.grid(row=2,column=1,sticky=N+S+E+W)
t1 = Text(f1,wrap="word")
t1.grid(row=3,column=0,sticky=N+S+E+W)
t2 = text.text_window(f2)

window.title("CYEN Marble Maze 1.0")
f1.pack()
window.mainloop()
print(correctpath)
while True:
    def check(ballmotion):
        for x in range(0,len(correctpath)):
            for a in range(0,len(ballmotion)):
                if ballmotion[a] == correctpath[a]:
                    t1.insert("end","You are on the correct path")




    if GPIO.input(17):
        ballmotion.append(17)
        sleep(1)
    if GPIO.input(12):
        ballmotion.append(12)
        sleep(1)
    if GPIO.input(27):
        ballmotion.append(27)
        sleep(1)
    if GPIO.input(23):
        ballmotion.append(23)
        sleep(1)
    if GPIO.input(25):
        ballmotion.append(25)
        sleep(1)
    if GPIO.input(21):
        ballmotion.append(21)
        sleep(1)








