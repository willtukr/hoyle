import pandas as pd
import numpy as np
import scipy
import hoy
import hoymath
import settings
import math
from chiplotle import *

'''Macro Drawing Functions'''

def pointGroup(name):
    for p in hoy.hoyle.loc[name]['pos']:
        point(p[0], p[1])


'''
Primitve Drawing Functions
'''

def line(x1, y1, x2, y2):
    settings.commands.append(hpgl.PU([(x1, y1)]))
    settings.commands.append(hpgl.PD([(x2, y2)]))

def point(x, y):
    settings.commands.append(hpgl.PU([(x, y)]))
    settings.commands.append(hpgl.PD([(x, y)]))

def circle(x, y, radius):
    settings.commands.append(hpgl.PU([(x, y)]))
    settings.commands.append(hpgl.CI(radius))

def square(x, y, radius):
    settings.commands.append(hpgl.PU([(x - radius/2, y - radius/2)]))
    settings.commands.append(hpgl.PD())
    settings.commands.append(hpgl.PR([(radius, 0), (0, radius), (-radius, 0),                                      (0, -radius)]))

def rect(x, y, width, height):
    settings.commands.append(hpgl.PU([(x - width/2, y - height/2)]))
    settings.commands.append(hpgl.PD())
    settings.commands.append(hpgl.PR([(width, 0), (0, height), (-width, 0), (0, -height)]))

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    settings.commands.append(hpgl.PU([(x1, y1)]))
    settings.commands.append(hpgl.PA([(x2, y2), (x3, y3), (x4, y4)]))

def triangle(x1, y1, x2, y2, x3, y3):
    settings.commands.append(hpgl.PU([(x1, y1)]))
    settings.commands.append(hpgl.PA([(x2, y2), (x3, y3)]))

'''
Sandstroke Functions
'''

def sandLine(x1, y1, x2, y2, density):
    amount_points = int(hoymath.euclidDistance(x1, y1, x2, y2) / density)
    vec = findVec(x1, y1, x2, y2)
    for i in range(0, amount_points):
        dest = findDest(x1, y1, vec)
        point(dest[0], dest[1])

def findVec(x1, y1, x2, y2):
    u = x2 - x1
    v = y2 - y1
    return [u, v]

def findDest(x1, y1, vector):
    rand = np.random.rand()
    u = x1 + vector[0] * rand
    v = y1 + vector[1] * rand
    return [u, v]
