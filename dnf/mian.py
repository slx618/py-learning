import pyautogui
from time import time, sleep
import sys
sys.path.append(r'F:\WorkPlace\py-learning\dnf')
from ctl import Keys;



sleep(3)
keys = Keys()

# mouse movement
for i in range(100):
    keys.directMouse(-1 * i, 0)
    sleep(0.004)

# mouse keys
keys.directMouse(buttons=keys.mouse_rb_press)
sleep(0.5)
keys.directMouse(buttons=keys.mouse_lb_press)
sleep(2)
keys.directMouse(buttons=keys.mouse_lb_release)
sleep(0.5)
keys.directMouse(buttons=keys.mouse_rb_release)

# or
keys.directMouse(buttons=keys.mouse_lb_press | keys.mouse_rb_press)
sleep(2)
keys.directMouse(buttons=keys.mouse_lb_release | keys.mouse_rb_release)

# keyboard (direct keys)
keys.directKey("a")
sleep(0.04)
keys.directKey("a", keys.key_release)

# keyboard (virtual keys)
keys.directKey("a", type=keys.virtual_keys)
sleep(0.04)
keys.directKey("a", keys.key_release, keys.virtual_keys)

# queue of keys (direct keys, threaded, only for keybord input)
keys.parseKeyString("a_down,-4,a_up,0x01")  # -4 - pause for 4 ms, 0x00 - hex code of Esc

# queue of keys (virtual keys, threaded, only for keybord input)
keys.parseKeyString("vk,a_down,-4,a_up")  # -4 - pause for 4 ms
