from http import client
import pyautogui as _
import time
from client import Client

_my_client = Client()

class InstagramClient:
    def __init__(self) -> None:
        pass

    def _click_in_followers_button(self):
        time.sleep(2)
        _.moveTo(960, 400)
        time.sleep(1)
        _.click()

    # Assume we are loged in instagram
    def follow_from_profile_page(self):
        self._click_in_followers_button()


    def post_story(self):
        _my_client.open_mobile_mode()
        time.sleep(2)
        self.go_to_feed()
        time.sleep(4)
        _.moveTo(500, 345)
        time.sleep(2)
        #Open file searcher to get file
       
    def go_to_feed(self):
        _my_client.go_to("instagram.com")

    def go_to_profile(self):
        _my_client.go_to("instagram.com/%s", "theroothaus")