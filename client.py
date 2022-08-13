import pyautogui as _
import time

class Client:
    def __init__(self) -> None:
        pass

    def open_browser(self):
        #move to chrome
        _.moveTo(850, 1050)
        _.click()
        time.sleep(1)
        #select chrome profile
        _.moveTo(1350, 750)
        _.click()

    def go_to(self, to):
        #click on url input
        _.moveTo(350, 80)
        time.sleep(1)
        _.click()
        time.sleep(1)
        _.write(to, .2)
        time.sleep(1)
        _.press("enter")
    
    def open_mobile_mode(self):
       time.sleep(2)
       _.moveTo(500, 500)
       _.hotkey("ctrl", "shift", "i") 