import pyautogui

from ctl import hero
from ctl import tia
import pygetwindow
import pyscreeze
from time import sleep


if __name__ == '__main__':
    sleep(3)
    rst = pyscreeze.locateOnScreen('img.png')
    # center = pyautogui.center(rst)
    print(rst)
    # print(center)

    tia.Tia()
    # titles = pygetwindow.getAllTitles()
    # for title in titles:
    #     print(title)
    #     if title == '地下城与勇士':
            # pyautogui.press('i', 30)
            # dnf = pygetwindow.getWindowsWithTitle(title)[0]
            # dnf.activate()
            # h = hero.Summoner()

