import math
import hoy
import hoymath
import hoydraw
from chiplotle import *

'''Initializing command list, plotter and canvas'''
def init(w, h, mode):
    global commands, plotter
    commands = []
    plotter = instantiate_plotters(  )[0]
    initCanvas(w, h, mode)
    pickPen(1)

def initOffline(w, h, mode):
    global commands, plotter
    commands = []
    initCanvas(w, h, mode)
    pickPen(1)

'''Canvas Dimension Options'''

def findHeight(width):
    return (width / math.sqrt(2))

def initCanvas(width, height, mode):
    if mode == 0:
        h = findHeight(width)
        setCanvasDimensions(width, h)
    if mode == 1:
        setCanvasDimensions(width, height)

def setCanvasDimensions(width, height):
    '''Setting both axis to arbitrary units'''
    global commands
    commands.append(hpgl.SC([(0, width), (0, height)]))

'''Pen Options'''

def pickPen(number):
    '''Selecting pen by holder number'''
    global commands
    commands.append(hpgl.SP(number))


'''Visualization Options'''

def ioView():
    '''Printing to PDF'''
    global commands
    io.view(commands)

def plot():
    '''Plotting'''
    global commands, plotter
    plotter.write(commands)



