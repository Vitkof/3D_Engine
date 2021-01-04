import pygame as pg
import sys
from object3d import *

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 800, 600
        self.FPS = 60
        self.window = pg.display.set_mode(self.RESOLUTION, pg.RESIZABLE)
        self.W, self.H = 500, 400
        self.timer = pg.time.Clock()
        self.create_obj()
        #self.object = Object3D(self) без метода, тоже самое

    def draw(self):
        self.window.fill(color='darkgray')

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
        pg.display.set_caption(str(self.timer.get_fps()))
        self.timer.tick(self.FPS)

    def create_obj(self):
        self.object = Object3D(self)


if __name__ == "__main__":
    sr = SoftwareRender()
    while True:
        sr.draw()