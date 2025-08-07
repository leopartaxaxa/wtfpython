from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

with SB(uc=True, test=True) as pipit:


    url = "https://kick.com/brutalles"
    pipit.uc_open_with_reconnect(url, 4)
    pipit.sleep(4)
    pipit.uc_gui_click_captcha()
    pipit.sleep(1)
    pipit.uc_gui_handle_captcha()
    pipit.sleep(4)
    if pipit.is_element_present('button:contains("Accept")'):
        pipit.uc_click('button:contains("Accept")', reconnect_time=4)
    if pipit.is_element_visible('#injected-channel-player'):
        pipit2 = pipit.get_new_driver(undetectable=True)
        pipit2.uc_open_with_reconnect(url, 5)
        pipit2.uc_gui_click_captcha()
        pipit2.uc_gui_handle_captcha()
        pipit.sleep(10)
        if pipit2.is_element_present('button:contains("Accept")'):
            pipit2.uc_click('button:contains("Accept")', reconnect_time=4)
        while pipit.is_element_visible('#injected-channel-player'):
            pipit.sleep(10)
        pipit.quit_extra_driver()
    pipit.sleep(1)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/brutalles"
        pipit.uc_open_with_reconnect(url, 5)
        if pipit.is_element_present('button:contains("Accept")'):
            pipit.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            pipit2 = pipit.get_new_driver(undetectable=True)
            pipit2.uc_open_with_reconnect(url, 5)
            pipit.sleep(10)
            if pipit2.is_element_present('button:contains("Accept")'):
                pipit2.uc_click('button:contains("Accept")', reconnect_time=4)
            while pipit.is_element_visible(input_field):
                pipit.sleep(10)
            pipit.quit_extra_driver()
    pipit.sleep(1)

