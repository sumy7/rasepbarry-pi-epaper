# encoding: utf-8

import requests
import json

from lib.wave_share_43inch_epaper import *


class Weather():
    def __init__(self, left, top, logger):
        self.left = left
        self.top = top
        self.logger = logger

        self.city = '北京'
        self.temperature = "? ~ ?℃"
        self.weather = "??"
        self.wind = "????"
        self.pic = 'WYIN.BMP'

    def convert_weather_pic_code(self):
        cw_f = self.weather
        w_bmp = 'WYIN.BMP'
        if cw_f == '晴':
            w_bmp = 'WQING.BMP'
        elif cw_f == '多云' or cw_f == '阴':
            w_bmp = 'WYIN.BMP'
        elif '冰雹' in cw_f:
            w_bmp = 'WBBAO.BMP'
        elif '阵雨' in cw_f:
            w_bmp = 'WXYU.BMP'
        elif '雨' in cw_f:
            w_bmp = 'WYU.BMP'
        elif '雪' in cw_f:
            w_bmp = 'WXUE.BMP'
        elif '雾' in cw_f or '霾' in cw_f:
            w_bmp = 'WWU.BMP'
        self.pic = w_bmp

    def fetch_weather_data(self):
        response = requests.get('http://api.jirengu.com/getWeather.php', params={'city': self.city})
        json_str = response.text.encode(response.encoding).decode(response.apparent_encoding)
        self.logger.info("[WEATHER]fetch_weather_data -> {}".format(json_str.encode('utf-8')))
        json_data = json.loads(json_str)
        if json_data['error'] == 0:
            data = json_data['results'][0]["weather_data"][0]
            self.temperature = data['temperature']
            self.weather = data['weather']
            self.wind = data['wind']

    def update(self):
        self.fetch_weather_data()
        self.convert_weather_pic_code()

    def draw(self, screen):
        screen.set_ch_font_size(FONT_SIZE_32)
        screen.set_en_font_size(FONT_SIZE_32)
        screen.text(15, 220, self.city)
        screen.text(40, 460, self.weather)
        screen.text(40, 500, self.temperature)
        screen.text(40, 540, self.wind)
        screen.bitmap(20, 280, self.pic)
