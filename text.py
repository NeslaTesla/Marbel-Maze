from tkinter import *

def text_window(a):
    x = Text(a,wrap="word")
    x.grid(row=1,column=1,sticky=N+S+E+W)
    x.insert("end", ('\n'
                     'This marble maze is created by: \n'
                     'Xavier Lewis\n'
                     'Jeremiah Hall\n'
                     'Vanessa Coogler\n'
                     '    \n'
                     '    In this maze, there are two end points. At the start of each round, one of the two endpoints'
                     'will be chosen as the "correct" one. The player will have to figure out which exit is the correct'
                     'one based on the sounds from the piezospeaker and the directions shown on the GUI. The GUI will '
                     'show if a player is going in the right direction by sating "you are going in the right direction"'
                     'or by saying "you are going in the WRONG direction". Once the player has reached the correct'
                     'endpoint, the green LED will turn on and the piezospeaker will play a tune. \n '
                     '\n'
                     'Components:\n'
                     'Adafruit capacitive touch sensor ($7.95)\n'
                     'Handmade maze unit\n'
                     'LEDs\n'
                     'Piezospeaker\n'))
