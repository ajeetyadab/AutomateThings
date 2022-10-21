# hrd=116377,hrng=116374,prt=116373,pgm=116370,mdy=116368
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

lgdcodes_villages=dict(hrd='116377',hrng='116374',prt='116373',pgm='116370',mdy='116368')
avedak_ka_naam="प्रताप"
pita_pati_ka_naam="भीसम सिंह"
mobile_number="7065509579"
avedak_ka_pata="निवासी ग्राम पृथ्वी नगर"

#भाग - 2 मृतक / मृतका / विवाहिता / पुनर्विवाहिता खातेदार का विवरण जिसकी मृत्यु के उपरान्त उत्तराधिकार का दावा किया जाना है

khatedaar_ka_naam="भीसम सिंह"
male_female="1"             # पुरुष खातेदार के लिए 1 और महिला खातेदार के लिए 2 चुने
mrityu_tithi="10/08/2022"
pita_pati_sanrakshak="1"    #पिता  =1,पति =2,संरक्षक=3
khatedaar_ke_pita_pati_ka_naam="तीरथ सिंह"
mode_aquired="उत्तराधिकार से"         #उत्तराधिकार से,स्वंय अर्जित की हुई
gram_ka_naam=lgdcodes_villages["prt"] #lgd villge code


#भाग - 3 खातेदार  के स्वामित्व की भूमि का विवरण

disputed_gata=["125","126","123"]# टोटल गाटाओ की संख्या
disputed_lgd=lgdcodes_villages["prt"]
no_of_gata=str(len(disputed_gata))
gata_range=range(int(no_of_gata))



#वारिसों का विवरण


varis_name=["प्रताप","परमाल","गौरव","उर्मिला"]
no_varis=str(len(varis_name))
varis_range=range(len(varis_name))
varis_age=["38","33","28","50"]
prakriti=["पिता","पति","संरक्षक"]                          # पिता / पति / संरक्षक की प्रकृति का नाम
varis_pita_pati_name="भीसम सिंह"                         #पिता / पति / संरक्षक का नाम
sambandh=["पुत्र-पृत्रादि क्रम में पुंजातीय वंशज","विधवा","अविवाहिता पुत्री","विवाहिता पूत्री"]



driver = webdriver.Firefox(executable_path=r"C:/Users/acer/PycharmProjects/AutomateThings/geckodriver.exe")

def load_login_page():
    driver.get("http://vaad.up.nic.in/Lekhpal_Login.aspx")
    time.sleep(5)
    select_mandal=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_ddl_court_mandal_U\"]"))
    select_mandal.select_by_value("13")
    time.sleep(2)
    select_janpad=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_Dropdown_New_Dist_U\"]"))
    select_janpad.select_by_value("136")
    time.sleep(2)
    select_tehsil=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_DropDownList_New_Tehsil_U\"]"))
    select_tehsil.select_by_value("00723")
    time.sleep(2)
    select_halka=Select(driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_User_type\"]"))
    select_halka.select_by_value("0113600723036")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id=\"ctl00_ContentPlaceHolder_revcourt_txt_password\"]").send_keys("@jIt4hero")
    time.sleep(2)
    txt=driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_captcha_lbl\"]").get_attribute("value")
    driver.find_element(By.XPATH, "//*[@id=\"ctl00_ContentPlaceHolder_revcourt_txt_captcha\"]").send_keys(txt)
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[@id=\"ctl00_ContentPlaceHolder_revcourt_btn_submit\"]").click()




def load_avedan_page():
    time.sleep(3)
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
    time.sleep(2)
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

    driver.find_element(By.XPATH,"//*[@id=\"txt_Applicant_Name_U\"]").send_keys(khatedaar_ka_naam)
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
    Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_SampattiShrot\"]")).select_by_value(mode_aquired)
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

def avedan_fourth_page():
    time.sleep(10)
    Select(driver.find_element(By.XPATH,"//*[@id=\"txt_dispute_div_bhaag3\"]")).select_by_value("00063")
    time.sleep(2)
    Select(driver.find_element(By.XPATH,"//*[@id=\"dropdown_village_bhaag3\"]")).select_by_value(disputed_lgd)
    time.sleep(2)
    Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_total_disputed_land\"]")).select_by_value(no_of_gata)
    time.sleep(3)
    for i in gata_range:
        driver.find_element(By.XPATH,"//*[@id=\"txt_gata_type_val\"]").send_keys(disputed_gata[i])
        time.sleep(3)
        # driver.find_element(By.XPATH,"//*[@id=\"txt_gata_type_val\"]").send_keys(int(disputed_gata[i]))
        driver.find_element(By.XPATH,"/html/body/form/div[4]/div/table/tbody/tr/td/table/tbody/tr[2]/td/fieldset/table/tbody/tr[2]/td/table/tbody/tr[4]/td[1]").click()
        select = Select(driver.find_element(By.ID, "ddl_gata_sankhya"))
        options = select.options
        print(options)
        for index in range(0, len(options) - 1):
            el = select.select_by_index(index)
            el.click()
            print(el)
            break
        break

        # time.sleep(3)
        # Select(driver.find_element(By.XPATH,"//*[@id=\"ddl_gata_sankhya\"]")).select_by_index(1)
        # time.sleep(2)











def avedan_fifth_page():
    Select(driver.find_element(By.XPATH,"//*[@id=\"ddlVarisoKisankhya\"]")).select_by_value(no_varis)
    time.sleep(2)
    for i in varis_range:
        driver.find_element(By.XPATH,"//*[@id=\"txt_Bhaag4_Name\"]").send_keys(varis_name[i])
        Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_PitaPatiSanrakshak\"]")).select_by_value(prakriti[0])
        driver.find_element(By.XPATH,"//*[@id=\"txt_Bhaag4_f_Name\"]").send_keys(varis_pita_pati_name)
        Select(driver.find_element(By.XPATH, "//*[@id=\"ddl_Bhaag4_Age\"]")).select_by_value(varis_age[i])
        Select(driver.find_element(By.XPATH, "//*[@id=\"txt_Bhaag4_KhaatedarSeSambandh\"]")).select_by_value(sambandh[0])

        driver.find_element(By.XPATH,"//*[@id=\"txt_waris_address\"]").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"txt_waris_address\"]").send_keys(avedak_ka_pata)
        driver.find_element(By.XPATH,"//*[@id=\"btn_AddVaarisKaVivaran\"]").click()
        time.sleep(3)















load_login_page()
load_avedan_page()
avedan_second_page()
avedan_third_page()
avedan_fourth_page()
# avedan_fifth_page()
