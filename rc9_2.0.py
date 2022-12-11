import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as e
# from selenium.webdriver.common.service import Service
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.chrome.options import Options
import time

# importing excel functions
from xutility import read_data

os.getcwd()

ser_ob = Service(r"C:/Users/acer/Desktop/python codes/geckodriver.exe")
driver = webdriver.Firefox(service=ser_ob)
wait = WebDriverWait(driver, 3)
# dictionary
file = "C:/Users/acer/Desktop/python codes/virasat_apps.xlsx"
virasat_dict = {
    1: [read_data(file, 'Sheet1', 23, 2), read_data(file, 'Sheet1', 23, 3), read_data(file, 'Sheet1', 23, 4),
        read_data(file, 'Sheet1', 23, 5), read_data(file, 'Sheet1', 23, 6)],
    2: [read_data(file, 'Sheet1', 24, 2), read_data(file, 'Sheet1', 24, 3), read_data(file, 'Sheet1', 24, 4),
        read_data(file, 'Sheet1', 24, 5), read_data(file, 'Sheet1', 24, 6)],
    3: [read_data(file, 'Sheet1', 25, 2), read_data(file, 'Sheet1', 25, 3), read_data(file, 'Sheet1', 25, 4),
        read_data(file, 'Sheet1', 25, 5), read_data(file, 'Sheet1', 25, 6)],
    4: [read_data(file, 'Sheet1', 26, 2), read_data(file, 'Sheet1', 26, 3), read_data(file, 'Sheet1', 26, 4),
        read_data(file, 'Sheet1', 26, 5), read_data(file, 'Sheet1', 26, 6)],
    5: [read_data(file, 'Sheet1', 27, 2), read_data(file, 'Sheet1', 27, 3), read_data(file, 'Sheet1', 27, 4),
        read_data(file, 'Sheet1', 27, 5), read_data(file, 'Sheet1', 27, 6)],
    6: [read_data(file, 'Sheet1', 28, 2), read_data(file, 'Sheet1', 28, 3), read_data(file, 'Sheet1', 28, 4),
        read_data(file, 'Sheet1', 28, 5), read_data(file, 'Sheet1', 28, 6)],
    7: [read_data(file, 'Sheet1', 29, 2), read_data(file, 'Sheet1', 29, 3), read_data(file, 'Sheet1', 29, 4),
        read_data(file, 'Sheet1', 29, 5), read_data(file, 'Sheet1', 29, 6)],

}

# data

avedak_ka_naam = read_data(file, 'Sheet1', 2, 2)
pita_pati_ka_naam = read_data(file, 'Sheet1', 3, 2)
mobile_number = read_data(file, 'Sheet1', 4, 2)
avedak_ka_pata = read_data(file, 'Sheet1', 5, 2)

male_female = read_data(file, 'Sheet1', 8, 2)
khatedaar_ka_naam = read_data(file, 'Sheet1', 9, 2)
mrityu_tithi = read_data(file, 'Sheet1', 10, 2)
# mrityu_tithi="07/12/2022"
pita_pati_sanrakshak = read_data(file, 'Sheet1', 11, 2)
khatedaar_ke_pita_pati_ka_naam = read_data(file, 'Sheet1', 12, 2)
mode_aquired = read_data(file, 'Sheet1', 13, 2)
gram_ka_naam = read_data(file, 'Sheet1', 14, 2)

disputed_lgd = read_data(file, 'Sheet1', 17, 2)
print(disputed_lgd)
no_of_gata = str(read_data(file, 'Sheet1', 18, 2))

disputed_gata = read_data(file, 'Sheet1', 19, 2).split(",")
print(disputed_gata)

no_varis = str(read_data(file, 'Sheet1', 22, 2))
print(virasat_dict[1])


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
        print(captcha)
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_txt_captcha").send_keys(captcha)
        driver.find_element(By.ID, "ctl00_ContentPlaceHolder_revcourt_btn_submit").click()

        """ctl00_ContentPlaceHolder_revcourt_lbl_msg"""
        try:
            wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder_revcourt_lbl_msg")))
        except e:
            is_logout = False


def load_mainpage():
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id=\"menu\"]/ul/li[5]/a/span").click()

    # avedan_second page

    driver.find_element(By.XPATH, "//*[@id=\"txt_Applicant_Name\"]").send_keys(avedak_ka_naam)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"txt_Applicant_f_Name\"]").send_keys(pita_pati_ka_naam)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"rb_Aavedak_UP_No\"]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id=\"txt_Aavedak_MobileNo\"]").send_keys(mobile_number)
    time.sleep(1)
    select_mandal = Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_court_mandal_A\"]"))
    select_mandal.select_by_value("13")
    time.sleep(2)
    select_janpad = Select(driver.find_element(By.XPATH, "//*[@id=\"Dropdown_New_Dist_A\"]"))
    select_janpad.select_by_value("136")
    time.sleep(1)

    select_tehsil = Select(driver.find_element(By.XPATH, "//*[@id=\"DropDownList_New_Tehsil_A\"]"))
    select_tehsil.select_by_value("00723")
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"txt_Applicant_Address\"]").send_keys(avedak_ka_pata)
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"btn_bhaag1_save\"]").click()


def load_third_page():
    select_gender = Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_Gender\"]"))
    select_gender.select_by_visible_text(male_female)
    time.sleep(1)

    select_reason_of_virasat = Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_KhatedaarType\"]"))
    select_reason_of_virasat.select_by_value("खातेदार की मृत्यु")
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"txt_Applicant_Name_U\"]").send_keys(khatedaar_ka_naam)
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"rbtn_cause_of_death\"]/tbody/tr/td[2]/label").click()
    time.sleep(1)

    select_date = Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_khatedaar_Tithi\"]"))
    select_date.select_by_value("खातेदार की मृत्यु की तिथि")
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"txt_new_filling_dt\"]").send_keys(mrityu_tithi)
    time.sleep(1)
    select_pita_pati = Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_f__type\"]"))
    select_pita_pati.select_by_visible_text(pita_pati_sanrakshak)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"txt_Applicant_f_Name_U\"]").send_keys(khatedaar_ke_pita_pati_ka_naam)
    Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_SampattiShrot\"]")).select_by_visible_text(mode_aquired)
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_court_mandal_U\"]")).select_by_value("13")  # mandal
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"Dropdown_New_Dist_U\"]")).select_by_value("136")  # janpad
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"DropDownList_New_Tehsil_U\"]")).select_by_value("00723")  # tehsil
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"txt_dispute_div\"]")).select_by_value("00063")  # paragna
    time.sleep(1)

    graam_name = Select(driver.find_element(By.XPATH, "//*[@id=\"dropdown_village\"]"))  # gram
    graam_name.select_by_visible_text(gram_ka_naam)

    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"txt_Applicant_Address_U\"]").send_keys(avedak_ka_pata)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"txt_JiskaVivaran_MobileNo\"]").send_keys(mobile_number)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"btn_bhaag2_save\"]").click()


def load_fourth_page():
    time.sleep(5)
    Select(driver.find_element(By.XPATH, "//*[@id=\"txt_dispute_div_bhaag3\"]")).select_by_value("00063")
    time.sleep(2)
    Select(driver.find_element(By.XPATH, "//*[@id=\"dropdown_village_bhaag3\"]")).select_by_visible_text(disputed_lgd)
    time.sleep(3)
    Select(driver.find_element(By.ID, "ddl_total_disputed_land")).select_by_visible_text(no_of_gata)
    time.sleep(5)
    for i in disputed_gata:
        driver.find_element(By.XPATH, "//*[@id=\"txt_gata_type_val\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"txt_gata_type_val\"]").send_keys(i)
        time.sleep(3)
        driver.find_element(By.XPATH,
                            "/html/body/form/div[4]/div/table/tbody/tr/td/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr[4]/td[1]").click()
        select = Select(driver.find_element(By.ID, "ddl_gata_sankhya"))
        select.select_by_index(1)
        time.sleep(1)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # for scrolling to take screenshot
    driver.save_screenshot("C:/Users/acer/Desktop/विरासत/virasat1.png")  # screenshot
    driver.find_element(By.XPATH, "//*[@id=\"btn_bhaag3_save\"]").click()


def load_final_page():
    time.sleep(2)
    Select(driver.find_element(By.XPATH, "//*[@id=\"ddlVarisoKisankhya\"]")).select_by_value(no_varis)
    for i in range(1, int(no_varis) + 1):
        driver.find_element(By.XPATH, "//*[@id=\"txt_Bhaag4_Name\"]").send_keys(virasat_dict[i + 1][0])
        Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_PitaPatiSanrakshak\"]")).select_by_visible_text(
            virasat_dict[i + 1][1])
        driver.find_element(By.XPATH, "//*[@id=\"txt_Bhaag4_f_Name\"]").send_keys(virasat_dict[i + 1][2])
        Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_Bhaag4_Age\"]")).select_by_value(
            str(virasat_dict[i + 1][3]))
        Select(driver.find_element(By.XPATH, "//*[@id=\"txt_Bhaag4_KhaatedarSeSambandh\"]")).select_by_visible_text(
            virasat_dict[i + 1][4])

        driver.find_element(By.XPATH, "//*[@id=\"txt_waris_address\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"txt_waris_address\"]").send_keys(avedak_ka_pata)
        driver.find_element(By.XPATH, "//*[@id=\"btn_AddVaarisKaVivaran\"]").click()
        time.sleep(3)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")  # for scrolling to take screenshot
    driver.save_screenshot("C:/Users/acer/Desktop/विरासत/virasat2.png")


load_login_page()
load_mainpage()
load_third_page()
load_fourth_page()
load_final_page()







