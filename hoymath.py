import pandas as pd
import numpy as np
import math
import hoy
import hoydraw
import settings

'''
Mathematical Functions
'''

def translate(point, amt_x, amt_y):
    x = point[0] + amt_x
    y = point[1] + amt_y
    return [x, y]

def rotate(point, theta):
    u = (point[0] * math.cos(theta)) - (point[1] * math.sin(theta))
    v = (point[0] * math.sin(theta)) + (point[1] * math.cos(theta))
    return [u, v]

def euclidDistance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2-y1), 2))

def convert3Dto2D(x, y, z, w, h):
    '''Converts a 3d point to 2d space with isometric projection'''
    a = math.radians(30)
    u = x * math.cos(a) + y * math.cos(a + math.radians(120)) + z * math.cos(a - math.radians(120))
    v = x * math.sin(a) + y * math.sin(a + math.radians(120)) + z * math.sin(a - math.radians(120))
    u += w / 2
    v += h / 2
    return [u, v]
