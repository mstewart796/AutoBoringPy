"""Control GUI via mouse"""
import pyautogui

# View size of screen
print(pyautogui.size())
width, height = pyautogui.size()
print(width)
print(height)

# View position
print(pyautogui.position())

# Move mouse instantly
# pyautogui.moveTo(10, 10)

# Move mouse slower
# pyautogui.moveTo(10, 10, duration=1.5)

# Move relatively from current position
# pyautogui.moveRel(200, 0, duration=2)

# Click
# pyautogui.click(1507, 38)
