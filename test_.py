import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


def test_is_opened(driver):
    driver.get("https://www.google.com/")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.google.com/"))

def test_assert():
    assert 4 == 4