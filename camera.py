import math
import numpy as np
import pygame as pg
from matrixs import *


# 1) Локальное пространство(все вершины относительно центра объекта)
#        >>> [Model Matrix] >>>
# 2) Мировое пространство(все вершины относительно центра мира)
#        >>> [Camera Matrix] >>>
# 3) Камеры система координат(все вершины относительно камеры)

class Camera:
    def __init__(self, render, position):
        self.render = render
        self.pos = np.array(position + [1.0])

        # Вектора ориентации камеры
        self.right = np.array([1, 0, 0, 1])
        self.up = np.array([0, 1, 0, 1])
        self.forward = np.array([0, 0, 1, 1])

        # Horizon & Vertical области видимости  камеры
        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.HEIGHT / render.WIDTH)
        # Ближняя и Дальняя области плоскости усеченной пирамиды обзора
        self.near_plane = 0.1
        self.far_plane = 100

    def translate_matrix(self):
        x, y, z, w = self.pos
        T = np.array([(1, 0, 0, 1),
                      (0, 1, 0, 1),
                      (0, 0, 1, 1),
                      (-x, -y, -z, 1)])
        return T

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        ux, uy, uz, w = self.up
        fx, fy, fz, w = self.forward
        R = np.array([[rx, ux, fx, 0],
                      [ry, uy, fy, 0],
                      [rz, uz, fz, 0],
                      [0, 0, 0, 1]])
        return R

    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()
