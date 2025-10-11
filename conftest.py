# conftest.py — только фикстуры/хуки
import pytest
from helpers.driver_factory import make_driver

@pytest.fixture
def driver():
    drv = make_driver()
    drv.maximize_window()
    yield drv
    drv.quit()