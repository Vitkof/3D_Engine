import math
import numpy as np


class Projection:
    def __init__(self, render):
        NEAR = render.camera.near_plane
        FAR = render.camera.far_plane
        RIGHT = math.tan(render.camera.h_fov / 2)
        TOP = math.tan(render.camera.v_fov / 2)
        LEFT = -RIGHT
        BOTTOM = -TOP

        # 1) Локальное пространство(все вершины относительно центра объекта)
        #        >>> [Model Matrix] >>>
        # 2) Мировое пространство(все вершины относительно центра мира)
        #        >>> [Camera Matrix] >>>
        # 3) Камеры система координат(все вершины относительно камеры)
        #        >>> [Projection Matrix] >>>
        # 4) Однородное пространство (все вершины находятся в небольшом кубе.
        #                             Все,что внутри куба - выводится на экран)

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * FAR * NEAR / (FAR - NEAR)

        self.M = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        #        >>> [Viewport Transform] >>>
        # 5) Матрица прееобразвания вершин в область экранных координат
        self.screen_matrix = np.array([
            [render.W_2, 0,          0, 0],
            [0,         -render.H_2, 0, 0],
            [0,          0,          1, 0],
            [render.W_2, render.H_2, 0, 1]
        ])
