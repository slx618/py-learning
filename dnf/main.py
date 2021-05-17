import pyautogui
import pygetwindow
from ctl import keys


if __name__ == '__main__':
    title = pygetwindow.getAllTitles()
    tt = pygetwindow.getAllWindows()
    handle = pygetwindow.getWindowsAt(100, 100)
    print(title)
    print(handle)

