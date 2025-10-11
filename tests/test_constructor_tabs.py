# tests/test_constructor_tabs.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from config import BASE_URL
from helpers.ui import wait_active_tab
from locators import TAB_SAUCES, TAB_FILLINGS, TAB_BUNS


class TestConstructorTabs:
    @pytest.mark.parametrize(
        "tab",
        [TAB_SAUCES, TAB_FILLINGS, TAB_BUNS],
        ids=["sauces", "fillings", "buns"],
    )
    def test_tab_switch(self, driver, tab):
        # открываем главную
        driver.get(BASE_URL + "/")

        # ждём нужный таб и крутим к нему
        tab_el = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(tab)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab_el)

        # кликаем по табу (если что — через JS)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab)).click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", tab_el)

        # базовое ожидание "какой-то таб стал активным"
        wait_active_tab(driver, timeout=5)

        # >>> ЯВНЫЙ ASSERT, что активен ИМЕННО наш таб <<<
        expected_text = tab_el.text.strip()

        # локатор активного контейнера для таба с нужным текстом:
        # - либо ancestor с role='tab', либо родительский контейнер,
        # - и он должен быть отмечен активным через aria-selected=true или класс '...current...'
        active_locator = (
            By.XPATH,
            "("
            f"//*[normalize-space()='{expected_text}']/ancestor::*[@role='tab'][1] | "
            f"//*[normalize-space()='{expected_text}']/parent::*"
            ")"
            "[ @aria-selected='true' "
            "  or contains(@class,'tab_tab_type_current') "
            "  or contains(@class,'current') ]"
        )

        active_container = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located(active_locator)
        )

        # sanity-check: внутри активного контейнера реально есть наш текст
        has_text_inside = bool(
            active_container.find_elements(
                By.XPATH, f".//*[normalize-space()='{expected_text}']"
            )
        ) or (expected_text in active_container.text.strip())

        assert has_text_inside, (
            f"Ожидали активный таб '{expected_text}', "
            f"но активен другой: '{active_container.text.strip()}'"
        )
