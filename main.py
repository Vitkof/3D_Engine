import pygame as pg
import sys
from object3d import *
from camera import *
from projection import *

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 800, 600
        self.FPS = 60
        self.window = pg.display.set_mode(self.RESOLUTION, pg.RESIZABLE)
        self.W_2, self.H_2 = self.WIDTH // 2, self.HEIGHT // 2
        self.timer = pg.time.Clock()
        self.create_obj()
        #self.object = Object3D(self) без метода, тоже самое

    def draw(self):
        self.window.fill(color='darkgray')
        self.object.screen_projection()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
        pg.display.set_caption(f"3D Engine [fps: {round(self.timer.get_fps(), 1)}]")
        self.timer.tick(self.FPS)

    def create_obj(self):
        self.camera = Camera(self, [0.5, 0.9, -2.5])
        self.projection = Projection(self)
        self.object = Object3D(self)
        self.object.rotate_Z(math.pi / 6)


if __name__ == "__main__":
    sr = SoftwareRender()
    while True:
        sr.draw()
