import pyautogui
import time

# time.sleep(2)

helpPos = pyautogui.locateOnScreen('./img.png')
print(helpPos)
#goPos = pyautogui.center(helpPos)
#pyautogui.moveTo(goPos, 2)
pyautogui.click(button="left")
# try:
#     while True:
#         newPos = pyautogui.position()
#         if point != newPos:
#             print(newPos)
#             point = newPos
# except KeyboardInterrupt:
#     print('\n Exit')