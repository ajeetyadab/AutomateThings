from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver_path = "./chromedriver"
driver = webdriver.Chrome(driver_path)

PASSWORD = "@jIt4hero"
DISTRICT_VALUE = "136"
TEHSHIL_VALUE = "00723"
HALKA_VALUE = "0113600723036"

number_x_path_map = {
    "1": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[1]/a/div",
    "2": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[2]/a/div",
    "3": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[3]/a/div",
    "4": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[4]/a/div",
    "5": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[1]/a/div",
    "6": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[2]/a/div",
    "7": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[3]/a/div",
    "8": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[4]/a/div",
    "9": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[1]/a/div",
    "0": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[2]/a/div",
    "delete": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[3]/a/div",
    "clear": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[4]/a/div"
}


def load_first_page():
    driver.get("https://upbhulekh.gov.in/khasra/homePage_login_khasra.jsp")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/center/main/div/div/ul/li[4]/a/div/div[1]").click()
    time.sleep(.25)


def load_second_page():
    selectDistrict = Select(driver.find_element(By.ID, "up_district"))
    selectDistrict.select_by_value(DISTRICT_VALUE)
    time.sleep(.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_tehsil"))
    selectTehsil.select_by_value(TEHSHIL_VALUE)
    time.sleep(.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_halka"))
    selectTehsil.select_by_value(HALKA_VALUE)
    time.sleep(.5)
    captcha_value = driver.find_element(By.ID, "CaptchaDiv").text
    driver.find_element(By.ID, "CaptchaInput").send_keys(captcha_value)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_third_page():
    time.sleep(20)
    # driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_fourth_page():
    time.sleep(10)
    # driver.find_element(By.XPATH, "//*[@id=\"link2\"]/a/div/div[2]").click()
    fill_form()


def fill_form():
    time.sleep(0.5)
    for i in range(1, 215):
        search_number(i)
        time.sleep(0.5)
        try:
            WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
            driver.find_element(By.NAME, "khata_number").click()
            driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[2]").click()
            fill_final_page()
        except TimeoutException as e:
            driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            time.sleep(3)


def click_digits(digits):
    for digit in digits:
        driver.find_element(By.XPATH, number_x_path_map[digit]).click()


def search_number(number):
    click_digits(str(number))
    driver.find_element(By.XPATH, "//*[@id=\"sgw\"]/button/i").click()


def fill_final_page():
    Select(driver.find_element(By.ID, "fasal_name")).select_by_value("56")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"tab-3\"]/form/p/table[3]/tbody/tr/td[1]/input[5]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"content\"]/center/header/div/div[7]/div").click()


load_first_page()
load_second_page()
load_third_page()
load_fourth_page()
