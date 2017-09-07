import pandas as pd
import numpy as np
import hoymath
import hoydraw
import settings


'''Data Initialization and Structure'''

def init():
    '''Initializes empty Hoyle'''
    global hoyle
    hoyle = pd.DataFrame()

def makeGroup(name, pos, vels, acc):
    '''Creates a new Group in Hoyle. Leave vels and acc as 0 if no physics involved'''
    global hoyle
    var = pd.Series([pos, vels, acc], index = ['pos', 'vels', 'acc'])
    var.name = name
    hoyle = hoyle.append(var)


'''Alterations'''

def group3DTo2D(name, width, height):
    '''Converts all points in a group from 3d to 2d space with isometric
    projection '''
    for p in hoyle.loc[name]['pos']:
        p = hoymath.convert3Dto2D(p[0], p[1], p[2], width, height)

def translateGroup(name, amount_x, amount_y):
    '''Translate all points in a group by some amount'''
    for p in hoyle.loc[name]['pos']:
        p = hoymath.translate(p, amount_x, amount_y)

def rotateGroup(name, center_of_rot, theta):
    translateGroup(name, -center_of_rot[0], -center_of_rot[1])
    for p in hoyle.loc[name]['pos']:
        p = hoymath.rotate(p, theta)
    translateGroup(name, center_of_rot[0], center_of_rot[1])


'''Data checking tools'''

def printGroup(name):
    '''Prints the attributes of a group to the console'''
    print hoyle.loc[name]

def printHoyle():
    '''Prints the entirety of the Hoyle'''
    print hoyle
