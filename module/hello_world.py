# encoding: utf-8
from lib.wave_share_43inch_epaper import FONT_SIZE_64


class HelloWorld():
    def __init__(self, left, top, logger):
        self.left = left
        self.top = top
        self.logger = logger

    def update(self):
        pass

    def draw(self, screen):
        screen.set_ch_font_size(FONT_SIZE_64)
        screen.set_en_font_size(FONT_SIZE_64)
        screen.text(self.left + 20, self.top + 20, "ＨＥＬＬＯ")
        screen.text(self.left + 20, self.top + 20 + 64 + 10, "ＷＯＲＬＤ！")
