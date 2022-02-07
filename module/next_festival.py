# coding=utf-8
import requests
import json
import time

from lib.wave_share_43inch_epaper import *
from utils.string_util import *


class NextFestival():

    def __init__(self, left, top, logger):
        self.left = left
        self.top = top
        self.logger = logger
        self.tts = "正在等待一个伟大的预言。。。"

    def fetch_tts_data(self):
        try:
            res = requests.get("http://timor.tech/api/holiday/tts?t={}".format(time.strftime("%Y%m%d", time.localtime())))
            self.logger.info("[NEXT_FESTIVAL]fetch_tts_data -> {}".format(res.text))
            data = json.loads(res.text)
            if data['code'] == 0:
                return data['tts']
            else:
                return "我本来想说点啥的，但是还是不说了吧。。。"
        except Exception:
            self.logger.error("[NEXT_FESTIVAL]Failed to fetch tts data.", exc_info=True)
            return "现在没有什么好说的，下次再说吧。。。"

    def update(self):
        self.tts = self.fetch_tts_data()

    def draw(self, screen):
        screen.set_ch_font_size(FONT_SIZE_32)
        screen.set_en_font_size(FONT_SIZE_32)

        screen.text(self.left + 5, self.top + 7, "节假日预言")
        for i, value in enumerate(chunk(self.tts, 17)):
            screen.text(self.left + 5, self.top + 7 + 32 * (i + 1) + 5, value)
