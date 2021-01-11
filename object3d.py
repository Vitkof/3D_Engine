import numpy as np
from matrixs import *
import pygame as pg
import math
import numba


@numba.njit(fastmath=True)
def any_func(polygon, W_2, H_2):
    return not np.any((polygon == W_2) | (polygon == H_2))

class Object3D:
    def __init__(self, render, peaks, faces):
        self.render = render
        # однородные к-ты v = (x,y,z,w), где w=1
        self.peaks = np.array([np.array(p) for p in peaks])
        self.faces = np.array([np.array(f) for f in faces])
        self.color = pg.color.Color('white')

        # self.peaks = np.array([
        #     (0,0,0,1), (0,1,0,1), (1,1,0,1), (1,0,0,1),
        #     (0,0,1,1), (0,1,1,1), (1,1,1,1), (1,0,1,1)
        # ])

        # self.faces = np.array([(0,1,2,3), (0,1,5,4), (0,4,7,3),
        #                        (6,5,4,7), (6,5,1,2), (6,2,3,7)])

    def move(self):
        kl = pg.key.get_pressed()
        if kl[pg.K_UP]:
            self.displaceIn([0,0,1])
        if kl[pg.K_DOWN]:
            self.displaceIn([0,0,-1])
        
    def screen_projection(self):
        peaks = self.peaks @ self.render.camera.camera_matrix()  # в пространствокамеры
        peaks = peaks @ self.render.projection.M                 # в однородное пространство (КУБ)
        w = np.reshape(peaks[:, -1], (-8, 1))  # (8,1)
        peaks /= w                             # Нормализация.Кор-ты вершины / W-координату
        peaks[(peaks > 1.5) | (peaks < -1.5)] = 0     # отсекаем вершины >1.5 и <-1.5 (-1,1)
        peaks = peaks @ self.render.projection.screen_matrix     # в экранное пространство
        peaks = peaks[:, 0:2]                                    # X и Y

        for face in self.faces:
            polygon = peaks[face]
            if any_func(polygon, self.render.W_2, self.render.H_2):
                pg.draw.polygon(self.render.window, self.color, polygon, 1)
        """
        for peak in self.peaks:
            #peak = peaks[peak]
            if not np.any((peak==self.render.W_2) | (peak==self.render.H_2)):
                pg.draw.circle(self.render.window, pg.color.Color('red'), peak, 5)
        """

    def displaceIn(self, pos):
        self.peaks = self.peaks @ displace(pos)

    def zoomIn(self, scale):
        self.peaks = self.peaks @ zoom(scale)

    def rotate_X(self, angle):
        self.peaks = self.peaks @ rotation_X(angle)

    def rotate_Y(self, angle):
        self.peaks = self.peaks @ rotation_Y(angle)

    def rotate_Z(self, angle):
        self.peaks = self.peaks @ rotation_Z(angle)


class Axes(Object3D):
    def __init__(self, render, p, f):
        super().__init__(render, p, f)
        self.peaks = np.array(p)
        self.faces = np.array(f)
        self.color = pg.Color("red")#[pg.Color('red'),pg.Color('green'),pg.Color('blue')]
        #self.color_faces = [(_c, _f) for _c, _f in zip(self.color, self.faces)]
