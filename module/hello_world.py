# encoding: utf-8
from lib.wave_share_43inch_epaper import *


class HelloWorld():
    def __init__(self, left, top, logger):
        self.left = left
        self.top = top
        self.logger = logger

    def update(self):
        pass

    def draw(self, screen):
        screen.set_ch_font_size(FONT_SIZE_32)
        screen.set_en_font_size(FONT_SIZE_32)
        screen.text(self.left + 20, self.top + 20, "ＨＥＬＬＯ")
        screen.text(self.left + 20, self.top + 20 + 32 + 10, "ＷＯＲＬＤ！")
