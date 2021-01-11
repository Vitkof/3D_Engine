import pygame as pg
import sys
from object3d import *
from camera import *
from projection import *


# Отсечение вершин при приближении реализовать, создание новыхвершин
class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1000, 600
        self.FPS = 60
        self.window = pg.display.set_mode(self.RESOLUTION, pg.RESIZABLE)
        self.W_2, self.H_2 = self.WIDTH // 2, self.HEIGHT // 2
        self.timer = pg.time.Clock()
        self.create_scene()

    def draw(self):
        self.window.fill(color='darkgray')
        self.camera.controller()
        self.object.screen_projection()
        self.object.move()

        self.axes.screen_projection()
        self.house.screen_projection()
        self.stryker.screen_projection()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if e.type == pg.MOUSEWHEEL:
                if e.y > 0:
                    self.camera.pos += self.camera.forward*3
                else:
                    self.camera.pos -= self.camera.forward*3
            if e.type == pg.MOUSEMOTION:
                if abs(e.rel[0]) > abs(e.rel[1]):
                    self.camera.camera_yaw(-e.rel[0]/100)
            if e.type == pg.MOUSEMOTION:
                if abs(e.rel[0]) <= abs(e.rel[1]):
                    self.camera.camera_ry(-e.rel[1] / 100)


        pg.display.update()
        pg.display.set_caption(f"3D Engine [fps: {round(self.timer.get_fps(), 1)}]")
        self.timer.tick(self.FPS)

    def create_scene(self):
        self.camera = Camera(self, [35, 5, -75])
        self.projection = Projection(self)

        self.object = self.import_model("models/m1.obj")
        self.object.zoomIn(0.12)
        self.object.displaceIn([65, 0, 10])
        self.house = self.import_model("models/farmhouse.obj")
        self.house.displaceIn([1,0,0])
        self.house.rotate_Y(math.pi / -1.5)
        self.stryker = self.import_model("models/stryker.obj")
        self.stryker.zoomIn(2.5)
        self.stryker.displaceIn([-10,0,-50])
        self.stryker.rotate_Y(math.pi)

        self.axes = Axes(self,
                         [(0,0,0,1), (1,0,0,1), (0,1,0,1), (0,0,1,1)],
                         [(0,1),(0,2),(0,3)])
        self.axes.zoomIn(30)


    def import_model(self, path):
        peaks, faces = [], []
        with open(path, 'r+') as file:
            for line in file:
                if line.startswith('v '):
                    peaks.append([float(l) for l in line.split()[1:]] + [1.0])
                elif line.startswith('f'):
                    _faces = line.split()[1:]
                    faces.append([int(_f.split('/')[0])-1 for _f in _faces])

        return Object3D(self, peaks, faces)


if __name__ == "__main__":
    sr = SoftwareRender()
    while True:
        sr.draw()
