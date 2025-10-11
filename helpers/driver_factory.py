# helpers/driver_factory.py — создание веб-драйвера (по env или с менеджером)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config import BROWSER, CHROMEDRIVER_PATH, EDGEDRIVER_PATH

def make_driver():
    if BROWSER == "edge":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option("excludeSwitches", ["enable-logging"])
        if EDGEDRIVER_PATH:  # путь задан переменной окружения
            service = EdgeService(executable_path=EDGEDRIVER_PATH)
        else:
            service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=opts)

    # chrome по умолчанию
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    if CHROMEDRIVER_PATH:  # путь задан переменной окружения
        service = ChromeService(executable_path=CHROMEDRIVER_PATH)
    else:
        service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)