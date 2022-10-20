from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

avedak_ka_naam="rahul"
pita_pati_ka_naam="hero"
mobile_number="7065509579"
avedak_ka_pata="hardaspur kothra"

#भाग - 2 मृतक / मृतका / विवाहिता / पुनर्विवाहिता खातेदार का विवरण जिसकी मृत्यु के उपरान्त उत्तराधिकार का दावा किया जाना है

khatedaar_ka_naam="raghu"

male_female="1"             # पुरुष खातेदार के लिए 1 और महिला खातेदार के लिए 2 चुने

mrityu_tithi="10/01/2022"

pita_pati_sanrakshak="1"    #पिता  =1,पति =2,संरक्षक=3

khatedaar_ke_pita_pati_ka_naam="zero"

mode_aquired="उत्तराधिकार से"         #उत्तराधिकार से,स्वंय अर्जित की हुई

gram_ka_naam="116377" #lgd villge code











driver_path = "./chromedriver"
driver = webdriver.Chrome(driver_path)

def load_login_page():
    driver.get("http://vaad.up.nic.in/Lekhpal_Login.aspx")
    time.sleep(1)
    select_mandal=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_ddl_court_mandal_U\"]"))
    select_mandal.select_by_value("13")
    time.sleep(1)
    select_janpad=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_Dropdown_New_Dist_U\"]"))
    select_janpad.select_by_value("136")
    time.sleep(1)
    select_tehsil=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_DropDownList_New_Tehsil_U\"]"))
    select_tehsil.select_by_value("00723")
    time.sleep(1)
    select_halka=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_User_type\"]"))
    select_halka.select_by_value("0113600723036")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"ctl00_ContentPlaceHolder_revcourt_txt_password\"]").send_keys("@jIt4hero")
    time.sleep(1)
    txt=driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_captcha_lbl\"]").get_attribute("value")
    print(txt)

    driver.find_element(By.XPATH, "//*[@id=\"ctl00_ContentPlaceHolder_revcourt_txt_captcha\"]").send_keys(txt)
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_btn_submit\"]").click()




def load_avedan_page():
    driver.find_element(By.XPATH,"//*[@id=\"menu\"]/ul/li[5]/a/span").click()

def avedan_second_page():
    driver.find_element(By.XPATH,"//*[@id=\"txt_Applicant_Name\"]").send_keys(avedak_ka_naam)
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id=\"txt_Applicant_f_Name\"]").send_keys(pita_pati_ka_naam)
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id=\"rb_Aavedak_UP_No\"]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id=\"txt_Aavedak_MobileNo\"]").send_keys(mobile_number)
    time.sleep(1)
    select_mandal=Select(driver.find_element(By.XPATH,"//*[@id=\"ddl_court_mandal_A\"]"))
    select_mandal.select_by_value("13")
    select_janpad = Select(driver.find_element(By.XPATH, "//*[@id=\"Dropdown_New_Dist_A\"]"))
    select_janpad.select_by_value("136")
    time.sleep(1)

    select_tehsil = Select(driver.find_element(By.XPATH,"//*[@id=\"DropDownList_New_Tehsil_A\"]"))
    select_tehsil.select_by_value("00723")
    time.sleep(1)

    driver.find_element(By.XPATH,"//*[@id=\"txt_Applicant_Address\"]").send_keys(avedak_ka_pata)
    time.sleep(1)

    driver.find_element(By.XPATH,"//*[@id=\"btn_bhaag1_save\"]").click()


def avedan_third_page():
    select_gender=Select(driver.find_element(By.XPATH,"//*[@id=\"ddl_Gender\"]"))
    select_gender.select_by_value(male_female)
    time.sleep(1)

    select_reason_of_virasat = Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_KhatedaarType\"]"))
    select_reason_of_virasat.select_by_value("खातेदार की मृत्यु")
    time.sleep(1)

    driver.find_element(By.XPATH,"//*[@id=\"txt_Applicant_Name_U\"]").send_keys(avedak_ka_naam)
    time.sleep(1)

    driver.find_element(By.XPATH, "//*[@id=\"rbtn_cause_of_death\"]/tbody/tr/td[2]/label").click()
    time.sleep(1)

    select_date=Select(driver.find_element(By.XPATH,"//*[@id=\"ddl_khatedaar_Tithi\"]"))
    select_date.select_by_value("खातेदार की मृत्यु की तिथि")
    time.sleep(1)

    driver.find_element(By.XPATH,"//*[@id=\"txt_new_filling_dt\"]").send_keys(mrityu_tithi)
    time.sleep(1)
    select_pita_pati=Select(driver.find_element(By.XPATH,"//*[@id=\"ddl_f__type\"]"))
    select_pita_pati.select_by_value(pita_pati_sanrakshak)
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id=\"txt_Applicant_f_Name_U\"]").send_keys(khatedaar_ke_pita_pati_ka_naam)
    Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_khatedaar_Tithi\"]")).select_by_value(mode_aquired)
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_court_mandal_U\"]")).select_by_value("13")#mandal
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"Dropdown_New_Dist_U\"]")).select_by_value("136")  # janpad
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"DropDownList_New_Tehsil_U\"]")).select_by_value("00723")  # tehsil
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"txt_dispute_div\"]")).select_by_value("00063")  # paragna
    time.sleep(1)
    Select(driver.find_element(By.XPATH, "//*[@id=\"dropdown_village\"]")).select_by_value(gram_ka_naam)  # gram
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"txt_Applicant_Address_U\"]").send_keys(avedak_ka_pata)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"txt_JiskaVivaran_MobileNo\"]").send_keys(mobile_number)
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id=\"btn_bhaag2_save\"]").click()









load_login_page()
load_avedan_page()
avedan_second_page()
avedan_third_page()