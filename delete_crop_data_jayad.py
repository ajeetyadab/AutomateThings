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
FASAL_NAME_VALUE = "5"
SICAHAI_VIDHI = "6"


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
    time.sleep(15)
    # select gram, fasal year, fasal  manually
    # driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_delete_page():
    time.sleep(10)
    # click manually on delete
    for i in range(1, 11):

        # if i in [23, 45, 46, 48]: # Ignore specific gatas
        #     continue
        search_number(i)
        try:
            WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
            driver.find_element(By.NAME, "khata_number").click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button").click()
            time.sleep(0.5)
            try:
                WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id=\"tab-3\"]/form/input[5]")))
                driver.find_element(By.XPATH, "//*[@id=\"tab-3\"]/form/input[5]").click()
            except TimeoutException as e:
                driver.find_element(By.XPATH, "//*[@id=\"content\"]/center/header/div/div[7]/div/a/i").click()
                continue
            time.sleep(0.5)
            # driver.find_element(By.XPATH, "//*[@id=\"content\"]/center/header/div/div[7]/div/a/i").click()
        except TimeoutException as e:
            driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
            time.sleep(1.5)


def click_digits(digits):
    for digit in digits:
        driver.find_element(By.XPATH, number_x_path_map[digit]).click()


def search_number(number):
    click_digits(str(number))
    driver.find_element(By.XPATH, "//*[@id=\"sgw\"]/button/i").click()



load_first_page()
load_second_page()
load_third_page()
load_delete_page()
