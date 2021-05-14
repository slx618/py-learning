import pyautogui

size = pyautogui.size()
point = pyautogui.position()

rst = pyautogui.onScreen(100, 100)

print(size, point, rst)

pyautogui.moveTo(10, 10, 2)
pyautogui.moveTo(size.width/2, size.height/2, 2)
pyautogui.moveRel(100, 0, 2)