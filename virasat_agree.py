import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as e
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.service import Service
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.chrome.options import Options
import time

# importing excel functions
from xutility import read_data

ser_ob = Service(r"C:/Users/acer/Desktop/python codes/geckodriver.exe")
driver = webdriver.Firefox(service=ser_ob)
wait = WebDriverWait(driver, 3)
# dictionary
file = "C:/Users/acer/Desktop/python codes/virasat_apps.xlsx"


village_virasat_xpaths={
"1":"//*[@id=\"GridView1_ctl02_hp_link_exceeded_time\"]",
"2":"//*[@id=\"GridView1_ctl03_hp_link_exceeded_time\"]",
"3":"//*[@id=\"GridView1_ctl04_hp_link_exceeded_time\"]",
"4":"//*[@id=\"GridView1_ctl05_hp_link_exceeded_time\"]",
"5":"//*[@id=\"GridView1_ctl06_hp_link_exceeded_time\"]"

}

def load_login_page():
    is_logout = True
    while is_logout:
        driver.get("http://vaad.up.nic.in/Lekhpal_Login.aspx")
        print(driver.title)
        time.sleep(2)
        mandal = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_ddl_court_mandal_U"))
        mandal.select_by_visible_text("मुरादाबाद")
        time.sleep(2)
        janpad = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_Dropdown_New_Dist_U"))
        janpad.select_by_visible_text("रामपुर")
        time.sleep(2)
        tehsil = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_DropDownList_New_Tehsil_U"))
        tehsil.select_by_visible_text("स्वार")
        time.sleep(2)
        halka = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_User_type"))
        halka.select_by_visible_text("हरदासपुर कोठरा / 0113600723036")
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_txt_password").send_keys("@jIt4hero")
        captcha = driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_captcha_lbl").get_attribute("value")
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_txt_captcha").send_keys(captcha)
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_btn_submit").click()

        """ctl00_ContentPlaceHolder_revcourt_lbl_msg"""
        try:
            wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder_revcourt_lbl_msg")))
        except e:
            is_logout = False


load_login_page()
for i in village_virasat_xpaths:
    driver.find_element(By.XPATH,village_virasat_xpaths[i]).click()
    time.sleep(3)
    try:
       driver.find_element(By.ID,"GridView1")
       driver.find_element(By.LINK_TEXT,"20221313600723001452")
       links=driver.find_elements(By.XPATH,"//table[@ID=\"GridView1\"]/tbody/tr/td")

    except NoSuchElementException:
        driver.find_element(By.XPATH,"/html/body/form/div[4]/div[1]/ul/li[1]/a").click()
        print(i)
        time.sleep(2)













# load_login_page()