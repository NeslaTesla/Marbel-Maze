import threading
from tkinter import *
from tkinter import scrolledtext
from mttkinter import mtTkinter
import text
import RPi.GPIO as GPIO
from time import sleep
from random import randint
from threading import *
from gpiozero import PWMOutputDevice

##GPIO.setup(19,GPIO.OUT)
class GUI:
    def __init__(self):
        self.window = mtTkinter.Tk()
        self.create_GUI()

    def switch(self):
        self.frame1.forget()
        self.frame2.pack()

    def switchBack(self):
        self.frame2.forget()
        self.frame1.pack()

    def reset(self):
        self.text1.delete("1.0","end")
        

    def create_GUI(self):
        self.frame1 = Frame(self.window)
        self.frame1.pack()
        self.frame2 = Frame(self.window)
        self.label = Label(self.frame1,text="MARBLE MAZE",font=("Courier",10))
        self.label.grid(row=0,column=1,sticky=N+S+E+W)
        self.infoB = Button(self.frame1, text="Info", font=("Courier",10), command=self.switch)
        self.infoB.grid(row=1,column=1,sticky=N+S+E+W)
        self.resetB = Button(self.frame1, text="Clear", font=("Courier",10), command=self.reset)
        self.resetB.grid(row=2,column=1,sticky=N+S+E+W)
        self.backB = Button(self.frame2,text="Back", font=("Courier",10), command=self.switchBack)
        self.backB.grid(row=0,column=1,sticky=N+S+E+W)
        self.text1 = scrolledtext.ScrolledText(self.frame1, wrap="word")
        self.text1.insert(END,"CHOOSE A PATH")
        self.scrollbar = Scrollbar
        self.text1.grid(row=4,column=1,sticky=N+S+E+W)
        self.text2 = text.text_window(self.frame2)
        #self.text1.insert("end",)

    def insertm(self,message):
        self.text1.insert(END,message + "\n")
        self.text1.see(END)

    def run(self):
        self.window.mainloop()

class PiezoSpeaker:
    def __init__(self,pin):
        self.piezo_pin = PWMOutputDevice(pin)

    def play_tone(self, frequency, duration):
        period = 1/ frequency
        duty_cycle = period / 2
        self.piezo_pin.value = duty_cycle
        sleep(duration)
        self.piezo_pin.value = 0

    def play_song(self, notes):
        for note in notes:
            frequency, duration = note
            self.play_tone(frequency, duration)

class gpio(threading.Thread):
    def __init__(self,pin1,pin2,pin3,pin4,pin5,pin6,pin7,pin8,pin9,gui):
        threading.Thread.__init__(self)
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.pin5 = pin5
        self.pin6 = pin6
        self.pin7 = pin7
        self.pin8 = pin8
        self.pin9 = pin9
##        self.pin10 = pin10
        self.gui = gui
        self.motion = []
        path1 = [12, 17]
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
        GPIO.setup(self.pin7,GPIO.OUT)
        GPIO.setup(self.pin8,GPIO.OUT)
        GPIO.setup(self.pin9,GPIO.IN)
##        GPIO.setup(self.pin10,GPIO.OUT)
##        pin16 = GPIO.PWM(self.pin10, 100)
##        pin16.start(50)

    def update(self):
        while True:
            GPIO.output(self.pin7, GPIO.HIGH)
            GPIO.output(self.pin8, GPIO.LOW)
##            for i in range(0,1):
##                self.gui.insertm(f"{self.correctpath}")
##                i+=1
            if GPIO.input(self.pin1):
##                self.gui.insertm(f"{self.correctpath}")
                self.motion.append(self.pin1)
                self.gui.insertm(f"{self.motion}")
##                GPIO.output(self.pin7, GPIO.LOW)
##                GPIO.output(self.pin8, GPIO.HIGH)
            if GPIO.input(self.pin2):
                self.motion.append(self.pin2)
##            if GPIO.input(self.pin9):
                self.gui.insertm(f"{self.motion}")
##                self.gui.insertm(f"{self.correctpath}")
            if GPIO.input(self.pin3):
                self.motion.append(self.pin3)
                self.gui.insertm(f"{self.motion}")
            if GPIO.input(self.pin4):
                self.motion.append(self.pin4)
                self.gui.insertm(f"{self.motion}")
            if GPIO.input(self.pin5):
                self.motion.append(self.pin5)
                self.gui.insertm(f"{self.motion}")
            if GPIO.input(self.pin6):
                self.motion.append(self.pin6)
                self.gui.insertm(f"{self.motion}")
            if len(self.motion)==1:
                a=0
                if (self.motion[0] == self.correctpath[0]) and a==0:
                    GPIO.output(self.pin7, GPIO.HIGH)
                    GPIO.output(self.pin8, GPIO.LOW)
##                    GPIO.output(self.pin10, GPIO.HIGH)
##                    pin16.ChangeFrequency(261.63)
                    self.gui.insertm("You are going the right direction")
##                    t1.root.quit()
                    a=+1
                    
                elif not (self.motion[0] == self.correctpath[0]):
                    self.gui.insertm("You are going the WRONG direction")
##                    t1.root.quit()
            if len(self.motion)==2:
                if (self.motion[1] == self.correctpath[0]):
                    self.gui.insertm("OKAY, NOW you are going in the right direction")
                if (self.motion[1] == self.correctpath[1]):
                    GPIO.output(self.pin7, GPIO.HIGH)
                    GPIO.output(self.pin8, GPIO.LOW)
                    self.gui.insertm("You are STILL going the right direction")
##                    t1.root.quit()
                    
##                else:
##                    self.gui.insertm("You are STILL going the WRONG direction")
####                    t1.root.quit()
            if len(self.motion)>=3:
                if (self.motion[-1] == self.correctpath[2]):
                    GPIO.output(self.pin8, GPIO.HIGH)
                    GPIO.output(self.pin7, GPIO.LOW)
                    self.gui.insertm("You have found the correct exit")
                    break
            sleep(.8)
        speaker = PiezoSpeaker(16)
        notes = [
            (261.63, 0.5),
##            (293.66, 0.5),
##            (329.63, 0.5),
##            (349.23, 0.5),
##            (392.23, 0.5),
##            (440.00, 0.5),
##            (493.88, 0.5),
            (523.25, 0.5),
        ]
        speaker.play_song(notes)

    def __del__(self):
        GPIO.cleanup()
            



if __name__ == '__main__':
    gui = GUI()
##    speaker = PiezoSpeaker(16)
    sensor_thread = gpio(17,12,27,21,23,25,19,18,5,gui)
    t2 = threading.Thread(target=gui.create_GUI)
    t1 = threading.Thread(target=sensor_thread.update)
    t1.setDaemon(True)
    t1.start()
    if (len(sensor_thread.motion)>2):
        if (sensor_thread.motion[-1] == sensor_thread.correctpath[2]):
            print("AMEN")
    ##    t2.start()
    gui.run()
    
    # window = Tk()
    # test = GUI(window)
    # window.mainloop()
