# encoding: utf-8

from lib.wave_share_43inch_epaper import *


class YearProgress:
    def __init__(self, left, top, logger):
        self.left = left
        self.top = top
        self.logger = logger

        self.year = 1990
        self.total_days = 365
        self.current_day_of_year = 1

    def update(self):
        date = time.localtime()
        year, month, day = date[:3]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_lunar_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        if is_lunar_year:
            self.total_days = 366
            month_days[1] = 29
        self.current_day_of_year = sum(month_days[:month - 1]) + day
        self.year = year

    def draw(self, screen):
        screen.set_ch_font_size(FONT_SIZE_32)
        screen.set_en_font_size(FONT_SIZE_32)

        total = 13
        used = int(total * (1.0 * self.current_day_of_year / self.total_days))
        un_used = total - used

        progress = "".join(['＊'] * used) + "".join(['－'] * un_used)

        screen.text(240, 220, "{}年进度".format(self.year))
        screen.text(240, 260, '0%')
        screen.text(710, 260, '100%')
        screen.text(300, 260, progress)
        screen.text(300, 300, "{}/{} {}%".format(self.current_day_of_year, self.total_days, int(self.current_day_of_year * 100 / self.total_days)))
