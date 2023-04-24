from tkinter import *

def text_window(a):
    x = Text(a,wrap="word")
    x.grid(row=1,column=1,sticky=N+S+E+W)
    x.insert("end", ('\n'
                     'This marble maze is created by: \n'
                     '    Xavier Lewis\n'
                     '    Jeremiah Hall\n'
                     '    Vanessa Coogler\n'
                     '    \n'
                     '    In this maze, the player must use the buttons on the GUI to control the maze to move, with the end goal of '
                     'helping the marble escape. This maze utilizes touch sensors, servos, and LED\'s to allow for a better user experience.'
                     'There is also an auto-solve feature that will use only the touch sensors to detect where the marble is and how '
                     'to get the marble to the goal. '))