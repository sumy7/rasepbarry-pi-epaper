import logging
import sys

from module.date_time import *
from module.framework_line import FrameworkLine
from module.hello_world import HelloWorld
from module.weather import *
from module.year_progress import YearProgress
from module.next_festival import NextFestival

reload(sys)
sys.setdefaultencoding('utf-8')

logfile = "log.txt"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=logfile,
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

GAP = 2

if __name__ == '__main__':
    logger.info("init")
    screen = Screen('/dev/ttyAMA0')
    screen.connect()
    time.sleep(GAP)
    screen.handshake()
    screen.clear()
    screen.set_memory(MEM_SD)
    screen.set_rotation(ROTATION_NORMAL)

    logger.info("load modules")
    modules = [DateTime(0, 0, logger),
               Weather(0, 0, logger),
               YearProgress(0, 0, logger),
               FrameworkLine(0, 0, logger),
               NextFestival(230, 340, logger),
               HelloWorld(230, 445, logger),
               ]
    for module in modules:
        module.update()
        module.draw(screen)

    logger.info("update screen")
    screen.set_ch_font_size(FONT_SIZE_64)
    screen.set_en_font_size(FONT_SIZE_64)
    screen.update()
    time.sleep(GAP)
    screen.disconnect()
    time.sleep(GAP)
    logger.info("Done")
