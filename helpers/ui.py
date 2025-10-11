# helpers/ui.py — простые UI-хелперы
from selenium.webdriver.support.ui import WebDriverWait

from locators import ACTIVE_TAB

def wait_active_tab(d, timeout=5):
    WebDriverWait(d, timeout).until(lambda drv: len(drv.find_elements(*ACTIVE_TAB)) > 0)