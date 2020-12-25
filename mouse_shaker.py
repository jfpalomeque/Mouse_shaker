import pyautogui
import time
pyautogui.FAILSAFE = False

print("Introduce number minutes the script will run. The script will start in 60 seconds")
minutes = float(input())

delay = 60
for i in range(delay):
    print(str(60 - i) + " seconds to start")
    time.sleep(1)


t_end = time.time() + 60 * minutes
print("starting")
while time.time() < t_end:
    pyautogui.moveRel(0, 10)
    pyautogui.moveRel(0, -10)
    print("Shaking, shaking")
    time.sleep(20)