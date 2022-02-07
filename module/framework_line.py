# coding=utf-8

class FrameworkLine():
    def __init__(self, left, top, logger):
        self.left = left
        self.top = top
        self.logger = logger

    def update(self):
        pass

    def draw(self, screen):
        screen.line(0, 200, 800, 200)
        screen.line(0, 201, 800, 201)

        screen.line(230, 200, 230, 600)

        screen.line(230, 340, 800, 340)
        screen.line(230, 490, 800, 490)
