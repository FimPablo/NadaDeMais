import pyautogui
import random
import time

def lol():
    screen_width, screen_height = pyautogui.size()

    while True:
        interval = random.uniform(30, 120)
        typeMove = random.randint(0, 1)
        
        time.sleep(interval)
        
        if typeMove:
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
        
            pyautogui.moveTo(x, y, duration=1.5)
            
            continue
        
        aQuant = random.randint(2, 20)
        
        pyautogui.write('8', interval=0.01)
        for _ in range(aQuant):
            pyautogui.write('=', interval=0.01)
            
        pyautogui.write('D', interval=0.01)


if __name__ == "__main__":
    lol()
# com carinho, Fim <3
