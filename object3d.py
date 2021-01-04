import numpy as np
from matrixs import *
import pygame as pg
import math


class Object3D:
    def __init__(self, render):
        self.render = render
        # однородные к-ты v = (x,y,z,w), где w=1
        self.vertexes = np.array([
            (0,0,0,1), (0,1,0,1), (1,1,0,1), (1,0,0,1),
            (0,0,1,1), (0,1,1,1), (1,1,1,1), (1,0,1,1)
        ])
        self.edges = np.array([[0, 1], [1, 2], [2, 3]])

        self.faces = np.array([(0,1,2,3), (0,1,5,4), (0,4,7,3),
                               (6,5,4,7), (6,5,1,2), (6,2,3,7)])

    def displace(self, pos):
        self.vertexes @= displace(pos)

    def zoomIn(self, scale):
        self.vertexes @= zoom(scale)

    def rotate_X(self, angle):
        self.vertexes @= rotation_X(angle)

    def rotate_Y(self, angle):
        self.vertexes @= rotation_Y(angle)

    def rotate_Z(self, angle):
        self.vertexes @= rotation_Z(angle)


x=4
print(pow(x, 0.5))
print(math.sqrt(x))