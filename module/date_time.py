# coding=utf-8
import datetime

from lib.wave_share_43inch_epaper import *
from lib.lunar import *


class DateTime(object):
    '''
    处理日期时间显示
    '''

    def __init__(self, left, top, logger):
        self.left = left
        self.top = top
        self.logger = logger

        self.time = '00:00'
        self.date = "1990-01-01"
        self.week = '星期一'
        self.luna_year = '戊戌[狗]'
        self.luna_date = '二零一八年九月初八'

    @staticmethod
    def get_datetime():
        time_now = datetime.now()
        time_string = time_now.strftime('%H:%M')
        date_string = time_now.strftime('%Y-%m-%d')
        week_string = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日'][time_now.isoweekday() - 1]
        return time_string, date_string, week_string

    def update(self):
        self.time, self.date, self.week = DateTime.get_datetime()
        (year, month, day) = get_ludar_date(datetime.now())
        self.luna_year = lunar_year(year)
        self.luna_date = '%s年%s%s' % (change_year(year), lunar_month(month), lunar_day(day))

    def draw(self, screen):

        clock_x = 10
        clock_y = 40
        temp_x = 0
        time_string = self.time
        date_string = self.date
        week_string = self.week
        self.logger.info("[DATETIME]time -> %s" % time_string)
        self.logger.info("[DATETIME]date -> %s" % date_string)
        self.logger.info("[DATETIME]week -> %s" % week_string)
        self.logger.info("[DATETIME]luna year -> %s" % self.luna_year)
        self.logger.info("[DATETIME]luna date -> %s" % self.luna_date)
        if time_string[0] == '0':
            time_string = time_string[1:]
            temp_x += 40
        for c in time_string:
            bmp_name = 'NUM{}.BMP'.format('S' if c == ':' else c)
            screen.bitmap(clock_x + temp_x, clock_y, bmp_name)
            temp_x += 70 if c == ':' else 100
        screen.set_ch_font_size(FONT_SIZE_48)
        screen.set_en_font_size(FONT_SIZE_48)
        screen.text(510, 40, date_string)
        screen.set_ch_font_size(FONT_SIZE_32)
        screen.set_en_font_size(FONT_SIZE_32)
        screen.text(500, 95, week_string)
        screen.text(650, 95, self.luna_year)
        screen.text(490, 150, self.luna_date)
