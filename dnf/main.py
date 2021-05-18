from ctl import keys
from time import sleep
from ctl import hero

if __name__ == '__main__':
    sleep(3)
    kb = keys.Keys()
    kb.directKey('up')
    kb.directKey('a')
    h = hero.Summoner()

    # titles = pygetwindow.getAllTitles()
    # for title in titles:
    #     print(title)
    #     if title == '微信':
    #         dnf = pygetwindow.getWindowsWithTitle(title)[0]
    #         dnf.activate()
    #         keyBord = keys.Keys()
    #         keyWork = keys.KeysWorker(keyBord)
    #         keyWork.sendKey(keyBord.dk['UP'], keyBord.direct_keys)

