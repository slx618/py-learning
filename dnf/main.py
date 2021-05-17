import pyautogui
import pygetwindow
from ctl import keys


if __name__ == '__main__':
    titles = pygetwindow.getAllTitles()
    for title in titles:
        print(title)
        if title == '地下城与勇士':
            dnf = pygetwindow.getWindowsWithTitle(title)[0]
            dnf.activate()
            keyBord = keys.Keys()
            keyWork = keys.KeysWorker(keyBord)
            keyWork.sendKey(keyBord.dk['UP'], keyBord.direct_keys)

