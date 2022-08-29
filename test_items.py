import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestMainPage1():

    def test_should_see_basket_button(self, browser):
        browser.get(link)
        #time.sleep(30)
        assert len(browser.find_elements(By.CSS_SELECTOR, ".btn.btn-primary")) == 1, 'Кнопка добавления товара в корзину отсутсвует'

