import pyautogui
from client import Client
from instagram_client import InstagramClient
import time
# height=1080
# WIDTH= 1920

#Define typing speed
#Define time to wait inter actions


def main():
    _ = Client()
    instagram_client= InstagramClient()
    # open browser
    _.open_browser()
    print("1. Browser Open")

    #go to website
    _.go_to("instagram.com/theroothaus")
    print("2. go to instagram page")

    
    instagram_client.post_story()


main()
