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
        self.h_FoV = math.pi / 3
        self.v_FoV = self.h_FoV * (render.HEIGHT / render.WIDTH)
        # Ближняя и Дальняя области плоскости усеченной пирамиды обзора
        self.near_plane = 0.1
        self.far_plane = 100
        # Скорость движения/вращения
        self.moving_speed = 1.1
        self.rotation_speed = 0.5   # в градусах

    def controller(self):
        kl = pg.key.get_pressed()
        if kl[pg.K_a]:
            self.pos -= self.right * self.moving_speed
        if kl[pg.K_d]:
            self.pos += self.right * self.moving_speed
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
        # if kl[pg.K_UP]:
        #     self.render.object.displaceIn([2,0,2])
        # if kl[pg.K_DOWN]:
        #     self.camera_pitch(-math.pi / 180 * self.rotation_speed)
        # if pg.event.get().type == pg.MOUSEWHEEL:
        #     self.pos += self.forward * 2
        # if ms[2]:
        #     self.pos -= self.forward * 2

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

    def camera_ry(self, angle):
        rtt = rotation_Axis(self.right[:-1], angle)
        self.right = self.right @ rtt
        self.up = self.up @ rtt
        self.forward = self.forward @ rtt

    def translate_matrix(self):
        x, y, z, w = self.pos
        T = np.array([(1, 0, 0, 1),
                      (0, 1, 0, 1),
                      (0, 0, 1, 1),
                      (-x,-y,-z,1)])
        return T

    def rotate_matrix(self):
        Rx, Ry, Rz, w = self.right
        Ux, Uy, Uz, w = self.up
        Fx, Fy, Fz, w = self.forward
        R = np.array([(Rx, Ux, Fx, 0),
                      (Ry, Uy, Fy, 0),
                      (Rz, Uz, Fz, 0),
                      (0, 0, 0, 1)])
        return R

    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()
