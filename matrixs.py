import numpy as np
import pygame as pg
from math import sin, cos

#  https://ru.wikipedia.org/wiki/Матрица_перехода
def displace(pos):
    """ [x',y',z'] = [x,y,z]*T """
    x, y, z = pos
    T = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1]
    ])
    return T

def rotation_X(a):
    """ [x',y',z'] = [x,y,z] * Rx """
    Rx = np.array([
        [1, 0, 0, 0],
        [0, cos(a), -sin(a), 0],
        [0, sin(a), cos(a), 0],
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
        [cos(a), -sin(a), 0, 0],
        [sin(a), cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return Rz

#  https://ru.wikipedia.org/wiki/Матрица_поворота#Матрица_поворота_вокруг_произвольной_оси
def rotation_Axis(v, a):
    # v = (x,y,z)
    x, y, z = v
    Ra = np.array([
        [cos(a)+(1-cos(a))*x**2, (1-cos(a))*x*y-sin(a)*z, (1-cos(a))*x*z+sin(a)*y, 0],
        [(1-cos(a))*y*x+sin(a)*z, cos(a)+(1-cos(a))*y**2, (1-cos(a))*y*z-sin(a)*x, 0],
        [(1-cos(a))*z*x-sin(a)*y, (1-cos(a))*z*y+sin(a)*x, cos(a)+(1-cos(a))*z**2, 0],
        [0, 0, 0, 1]
    ])

    # C, S = cos(a), sin(a)
    # iC = 1 - cos(a)
    # Ra = np.array([
    #     [x**2+(1-x**2)*C, iC*x*y-z*S, iC*x*z+y*S, 0],
    #     [iC*x*y+z*S, y**2+(1-y**2)*C, iC*y*z-x*S, 0],
    #     [iC*x*z-y*S, iC*y*z+x*S, z**2+(1-z**2)*C, 0],
    #     [0, 0, 0, 1]
    # ])
    return Ra

def zoom(x):
    """ [x',y',z'] = [x,y,z] * Z """
    Z = np.array([
        [x, 0, 0, 0],
        [0, x, 0, 0],
        [0, 0, x, 0],
        [0, 0, 0, 1]
    ])
    return Z
