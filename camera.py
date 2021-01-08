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
        # Скорость движения/вращения
        self.moving_speed = 0.02
        self.rotation_speed = 0.5   # в градусах

    def controller(self):
        kl = pg.key.get_pressed()
        if kl[pg.K_a]:
            self.pos += self.right * self.moving_speed
        if kl[pg.K_d]:
            self.pos -= self.right * self.moving_speed
        if kl[pg.K_w]:
            self.pos += self.forward * self.moving_speed
        if kl[pg.K_s]:
            self.pos -= self.forward * self.moving_speed
        if kl[pg.K_q]:
            self.pos -= self.up * self.moving_speed
        if kl[pg.K_e]:
            self.pos += self.up * self.moving_speed
        if kl[pg.K_LEFT]:
            self.camera_yaw(math.pi / 180 * self.rotation_speed)
        if kl[pg.K_RIGHT]:
            self.camera_yaw(-math.pi / 180 * self.rotation_speed)
        if kl[pg.K_UP]:
            self.camera_pitch(math.pi / 180 * self.rotation_speed)
        if kl[pg.K_DOWN]:
            self.camera_pitch(-math.pi / 180 * self.rotation_speed)

    def camera_pitch(self, angle):
        rtt = rotation_X(angle)
        self.right = self.right @ rtt
        self.up = self.up @ rtt
        self.forward = self.forward @ rtt

    def camera_yaw(self, angle):
        rtt = rotation_Y(angle)
        self.right = self.right @ rtt
        self.up = self.up @ rtt
        self.forward = self.forward @ rtt
        
    def camera_roll(self, angle):
        rtt = rotation_Z(angle)
        self.right = self.right @ rtt
        self.up = self.up @ rtt
        self.forward = self.forward @ rtt

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
