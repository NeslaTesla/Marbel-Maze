import threading
from tkinter import *
import text
import RPi.GPIO as GPIO
from time import sleep
from random import randint
from threading import *

class GUI:
    def __init__(self,master):
        self.window = Tk()
        self.master = master
        self.master.title('example')
        self.create_GUI()

    def switch(self):
        self.frame1.forget()
        self.frame2.pack()

    def switchBack(self):
        self.frame2.forget()
        self.frame1.pack()

    def create_GUI(self):
        self.frame1 = Frame(self.master)
        self.frame1.pack()
        self.frame2 = Frame(self.master)
        self.label = Label(self.frame1,text="MARBLE MAZE",font=("Courier",10))
        self.label.grid(row=0,column=1,sticky=N+S+E+W)
        self.infoB = Button(self.frame1, text="Info", font=("Courier",10), command=self.switch)
        self.infoB.grid(row=1,column=1,sticky=N+S+E+W)
        self.resetB = Button(self.frame1, text="Reset", font=("Courier",10),)
        self.resetB.grid(row=2,column=1,sticky=N+S+E+W)
        self.backB = Button(self.frame2,text="Back", font=("Courier",10), command=self.switchBack)
        self.backB.grid(row=0,column=1,sticky=N+S+E+W)
        self.text1 = Text(self.frame1, wrap="word")
        self.text1.grid(row=4,column=1,sticky=N+S+E+W)
        self.text2 = text.text_window(self.frame2)
        #self.text1.insert("end",)

    def insertm(self,message):
        self.text1.insert(END,message + "\n")

    def run(self):
        self.window.mainloop()



class gpio(threading.Thread):
    def __init__(self,pin1,pin2,pin3,pin4,pin5,pin6,gui):
        threading.Thread.__init__(self)
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.pin5 = pin5
        self.pin6 = pin6
        self.gui = gui
        self.motion = []
        path1 = [17, 12]
        end1 = 27
        path2 = [21, 25]
        end2 = 23
        paths = [path1, path2]
        self.correctpath = paths[randint(0,1)]
        self.state= "correct"
        if 17 in self.correctpath:
            self.correctpath.append(end1)
        else:
            self.correctpath.append(end2)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1,GPIO.IN)
        GPIO.setup(self.pin2,GPIO.IN)
        GPIO.setup(self.pin3,GPIO.IN)
        GPIO.setup(self.pin4,GPIO.IN)
        GPIO.setup(self.pin5,GPIO.IN)
        GPIO.setup(self.pin6,GPIO.IN)

    def update(self):
        while True:
            if GPIO.input(self.pin1):
                self.motion.append(self.pin1)
                self.gui.insertm(f"{self.motion}")
            sleep(3)



if __name__ == '__main__':
    gui = GUI()
    sensor_thread = gpio(17,12,27,21,23,25,gui)
    sensor_thread.start()
    gui.run()
    # window = Tk()
    # test = GUI(window)
    # window.mainloop()