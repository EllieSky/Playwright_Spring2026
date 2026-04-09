import os

from dotenv import load_dotenv

load_dotenv()

def get_browser_launch_options():
    return {"headless": os.getenv("HEADLESS", "TRUE").upper() == "TRUE",
            "slow_mo": int(os.getenv("SLOW_MO", "0"))
            }

def get_base_url():
    return os.getenv("BASE_URL", "https://nop-qa.portnov.com/").lower()

def get_browser_type():
    return os.getenv("BROWSER_TYPE", "chromium").lower()

def get_viewport_width():
    return int(os.getenv("VIEWPORT_WIDTH", "1920"))

def get_viewport_height():
    return int(os.getenv("VIEWPORT_HEIGHT", "1080"))



