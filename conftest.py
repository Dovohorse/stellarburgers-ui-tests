import os
import pathlib
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Базовый URL стенда
BASE_URL = os.getenv("SB_URL", "https://stellarburgers.nomoreparties.site")
# Браузер: chrome (дефолт) или edge
BROWSER = os.getenv("SB_BROWSER", "chrome").lower()

ROOT = pathlib.Path(__file__).resolve().parent

def _make_chrome():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Если chromedriver лежит рядом с проектом — используем его, иначе менеджер драйверов
    local_driver = ROOT / ("chromedriver.exe" if os.name == "nt" else "chromedriver")
    if local_driver.exists():
        service = ChromeService(executable_path=str(local_driver))
    else:
        service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)

def _make_edge():
    opts = webdriver.EdgeOptions()
    opts.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Главное: пробуем локальный msedgedriver.exe (лежит у тебя в корне)
    local_driver = ROOT / ("msedgedriver.exe" if os.name == "nt" else "msedgedriver")
    if local_driver.exists():
        service = EdgeService(executable_path=str(local_driver))
    else:
        service = EdgeService(EdgeChromiumDriverManager().install())
    return webdriver.Edge(service=service, options=opts)

@pytest.fixture
def driver():
    drv = _make_chrome() if BROWSER == "chrome" else _make_edge()
    drv.maximize_window()
    yield drv
    drv.quit()
