import pyautogui 

#print(pyautogui.size())
#width=1920, height=1080

x = 0

while x < 5:
    pyautogui.moveTo(100, 100, duration = 1) 
    pyautogui.moveTo(200, 200, duration = 1)
    #x = x + 1