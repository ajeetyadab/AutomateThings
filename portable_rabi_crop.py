from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException,NoAlertPresentException,UnexpectedAlertPresentException,NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

serv_obj=Service("chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
actions=ActionChains(driver)
mywait=WebDriverWait(driver,10)



#लेखपाल क विवरण 
KEY = "Renu@1234"
DISTRICT_VALUE = "136"
TEHSHIL_VALUE = "00723"
HALKA_VALUE = "0113600723038/ ढाैकपुरी टाण्‍डा"
VILLAGE_NAME = "116385/साल्वे नगर"
SICAHAI_VIDHI = "13"
RABI_VALUE = "रबी की फसल (1 जनवरी से 28 फरवरी)"
JAYAD_VALUE = ""

ttime = time.localtime()

fasal_dumy = " "
fasal = {"gehu":"गेहूँ अधिक उपज वाला",
         "makka":"मक्का",
         "matar":"मटर",
         "aalu" :"आलू",
         "pyaj":"प्याज",
         "others":"अन्य तरकारियाँ (भूमि के नीचे उपजने वाली जो भी सम्मलित हैं),",
         "lehsan":"लहसुन",
         "lahi" :"लाही",
         "sarso":"सरसों",
         "barseem":"वरसीम",
         "fodder":"अन्य चारा (नाम सहित),",
         "rikt" :"रिक्त"
         }


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

XPATH_MAPPING = {
    "SURAKSHIT_KAREIN_BUTTON": "//*[@id=\"submitBtn\"]",
    "BACK_BUTTON_ON_SICHAI_PAGE": "//*[@id=\"content\"]/center/header/div/div[7]/div/a"
}


def load_first_page():
    driver.get("http://164.100.59.148/")
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id=\"about_us\"]/div/div[2]/a").click()
    time.sleep(2)
    if ttime.tm_hour >=9 and ttime.tm_hour <= 16:
        driver.find_element(By.XPATH,"/html/body/center/main/div/div/ul/li[3]/a/div/div[1]").click() # 8- 5 pm link
        
		
    else:
        driver.find_element(By.XPATH,"/html/body/center/main/div/div/ul/li[5]/a/div/div[1]").click() # after 8 pm link
        
    
    time.sleep(1)



def load_second_page():
    selectDistrict = Select(driver.find_element(By.ID, "up_district"))
    selectDistrict.select_by_visible_text("रामपुर")
    time.sleep(1)
    selectTehsil = Select(driver.find_element(By.ID, "up_tehsil"))
    selectTehsil.select_by_visible_text("स्वार")
    
    
    time.sleep(.5)
    selecthalka = Select(driver.find_element(By.ID, "up_halka"))
    time.sleep(.5)
    selecthalka.select_by_visible_text(HALKA_VALUE)
    driver.find_element(By.ID, "password").send_keys(KEY)
    time.sleep(15)
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()



def load_third_page():
    time.sleep(2)
    Select(driver.find_element(By.ID,"gram_name")).select_by_visible_text(VILLAGE_NAME)
    time.sleep(2)
    
    Select(driver.find_element(By.ID,"fasalYear")).select_by_visible_text("1430 (1 जुलाई 2022 से 30 जून 2023)")
    time.sleep(3)
    #Select(driver.find_element(By.ID,"fasal")).select_by_visible_text("खरीफ की फसल (10 अगस्त से 30 सितम्बर)") # FOR KHAREEF
    Select(driver.find_element(By.ID,"fasal")).select_by_visible_text(RABI_VALUE) # FOR RABI
    
    time.sleep(1)
    alert_window_0 = driver.switch_to.alert
    print(alert_window_0.text)
    alert_window_0.accept()
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
    


def load_fourth_page():
    time.sleep(2)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    alert_window.accept()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id=\"link2\"]/a").click()
    for i in range(1,190):
        if i in [1,2,3,4,5]:#रिक्त 
            fill_rikt_pravisti(i)
            print(i)
            
            
        if i in []:#गेहू
            fasal_dumy = fasal["gehu"]
            fill_fasal_entry(i)
            print(i)
            
        
        if i in []:#लाही
            fasal_dumy = fasal["lahi"]
            fill_fasal_entry(i)
            print(i)
        
        if i in []:#अन्य तरकारी
            fasal_dumy = fasal["others"]
            fill_fasal_entry(i)
            print(i)
            
                
        if i in []:#चारा
            fasal_dumy = fasal["fodder"]
            fill_fasal_entry(i)
            print(i)
        
                    


def click_digits(digits):
    for digit in digits:
        driver.find_element(By.XPATH, number_x_path_map[digit]).click()


def search_number(number):
    click_digits(str(number))
    driver.find_element(By.XPATH, "//*[@id=\"sgw\"]/button/i").click()


def fill_fasal_entry(i):
    search_number(i)
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
        driver.find_element(By.NAME, "khata_number").click()
        driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[2]").click()
        time.sleep(0.5)
        Select(driver.find_element(By.ID, "fasal_name")).select_by_visible_text(fasal_dumy)#enter fasal name
        time.sleep(1)
        agri_area = driver.find_element(By.ID, "agriArea").get_attribute('value')
        Select(driver.find_element(By.ID, "agriTech")).select_by_value(SICAHAI_VIDHI)
        driver.find_element(By.ID, "sichitArea").clear()
        driver.find_element(By.ID, "sichitArea").send_keys(agri_area)
        driver.find_element(By.XPATH, XPATH_MAPPING["SURAKSHIT_KAREIN_BUTTON"]).click()
        time.sleep(.5)
        driver.find_element(By.XPATH, XPATH_MAPPING["BACK_BUTTON_ON_SICHAI_PAGE"]).click()
    except TimeoutException as e:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(0.5)


def fill_rikt_pravisti(i):
    search_number(i)
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
        driver.find_element(By.NAME, "khata_number").click()
        driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[2]").click()
        time.sleep(0.5)
        Select(driver.find_element(By.ID, "fasal_name")).select_by_visible_text(fasal["rikt"])
        #driver.find_element(By.XPATH, XPATH_MAPPING["SURAKSHIT_KAREIN_BUTTON"]).click()
        time.sleep(.5)
        driver.find_element(By.XPATH, XPATH_MAPPING["BACK_BUTTON_ON_SICHAI_PAGE"]).click()
    except TimeoutException as e:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(0.5)


load_first_page()
load_second_page()
load_third_page()
load_fourth_page()
