import pyautogui
import time

time.sleep(2)

pyautogui.PAUSE = 0.5

pyautogui.typewrite('i like python')

pyautogui.typewrite('\ni like python', 0.25)

pyautogui.typewrite(['enter', 'g', 'o', 'o', 'd', 'left', 'left', 'left', 'backspace', 'G', 'end', '.'], 0.25)

pyautogui.keyDown('shift')
pyautogui.press('enter')
pyautogui.keyUp('shift')

# pyautogui.keyDown('command')
# pyautogui.press('a')
# pyautogui.press('c')
# pyautogui.press('v')
# pyautogui.keyUp('command')

pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
pyautogui.click()
pyautogui.hotkey('command', 'v')
