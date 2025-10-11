# config.py — единая точка настроек
import os

BASE_URL = os.getenv("SB_URL", "https://stellarburgers.nomoreparties.site")
BROWSER = os.getenv("SB_BROWSER", "chrome").lower()

# Необязательные пути к локальным драйверам
CHROMEDRIVER_PATH = os.getenv("SB_CHROMEDRIVER_PATH")  # например: D:\drivers\chromedriver.exe
EDGEDRIVER_PATH = os.getenv("SB_EDGEDRIVER_PATH")      # например: D:\drivers\msedgedriver.exe