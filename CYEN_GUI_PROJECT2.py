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
correctpath = paths[randint(0,1)]
if 17 in correctpath:
    correctend = end1
else:
    correctend = end2

ballmotion = []
if GPIO.input(17):
    ballmotion.append(17)
window = Tk()

def switch():
    f2.pack()
    f1.forget()

def switchBack():
    f1.pack()
    f2.forget()



f1 = Frame(window)
f2 = Frame(window)
l1 = Label(f1, text="MARBLE MAZE", font=("Courier",30))
l1.grid(row=0,column=1,sticky=N+S+E+W)
infoB = Button(f1,text="Info",font=("Courier",10),command=switch)
infoB.grid(row=1,column=1,sticky=N+S+E+W)
backB = Button(f2,text="Back",font=("Courier",10),command=switchBack)
backB.grid(row=0,column=1,sticky=N+S+E+W)
t1 = text.text_window(f2)
print(ballmotion)



window.title("CYEN Marble Maze 1.0")
f1.pack()
window.mainloop()




