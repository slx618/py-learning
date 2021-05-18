from ctl import hero
import pygetwindow
from time import sleep

if __name__ == '__main__':
    h = hero.Summoner()
    sleep(3)

    titles = pygetwindow.getAllTitles()
    for title in titles:
        # print(title)
        if title == '微信':
            dnf = pygetwindow.getWindowsWithTitle(title)[0]
            dnf.activate()
            h = hero.Summoner()

