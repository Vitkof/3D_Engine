import numpy as np
import pygame as pg
from math import sin, cos

# https://ru.wikipedia.org/wiki/Матрица_перехода
def displace(pos):
    """ [x',y',z'] = [x,y,z]*T """
    a1, a2, a3 = pos
    T = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [a1, a2, a3, 1]
    ])
    return T

def rotation_X(a):
    """ [x',y',z'] = [x,y,z] * Rx """
    Rx = np.array([
        [1, 0, 0, 0],
        [0, cos(a), sin(a), 0],
        [0, -sin(a), cos(a), 0],
        [0, 0, 0, 1]
    ])
    return Rx

def rotation_Y(a):
    """ [x',y',z'] = [x,y,z] * Ry """
    Ry = np.array([
        [cos(a), 0, sin(a), 0],
        [0, 1, 0, 0],
        [-sin(a), 0, cos(a), 0],
        [0, 0, 0, 1]
    ])
    return Ry

def rotation_Z(a):
    """ [x',y',z'] = [x,y,z] * Rz """
    Rz = np.array([
        [cos(a), sin(a), 0, 0],
        [-sin(a), cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return Rz

def zoom(x):
    """ [x',y',z'] = [x,y,z] * Z """
    Z = np.array([
        [x, 0, 0, 0],
        [0, x, 0, 0],
        [0, 0, x, 0],
        [0, 0, 0, 1]
    ])
    return Z
