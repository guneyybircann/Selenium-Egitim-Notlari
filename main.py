from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
actions = ActionChains(driver)
driver.maximize_window()

# TRADINGVIEW ÖRNEĞİ
# driver.get("https://tr.tradingview.com/chart/?symbol=FX_IDC%3AXAUTRYG")
# driver.implicitly_wait(30)
#
# deger = driver.find_element(By.XPATH, '/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]')
# gecici_deger = None
#
# while 1:
#     suanki_deger = deger.text
#     if suanki_deger != gecici_deger:
#         print(suanki_deger)
#     gecici_deger = suanki_deger
#
#

# PRATİK SİTESİ ÖRNEĞİ
# driver.get("https://seleniumbase.io/demo_page")
# textInput = driver.find_element(By.ID, "myTextInput")
# textInput.send_keys("Selenium 101")
#
# textInput2 = driver.find_element(By.NAME, "preText2")
# print(textInput2.get_attribute("value"))
#
# placeHolder = driver.find_element(By.ID, "placeholderText")
# print(placeHolder.get_attribute("placeholder"))
# driver.execute_script(f"arguments[0].setAttribute('placeholder', 'Yeni placeholder yazısı');", placeHolder)
#
# svgRect = driver.find_element(By.ID, "svgRect")
# driver.execute_script("arguments[0].setAttribute('fill', '#FF5733');", svgRect)
# driver.execute_script("arguments[0].setAttribute('stroke-width', '10');", svgRect)
# driver.execute_script("arguments[0].setAttribute('stroke', 'blue');", svgRect)
#
# sleep(2)
# select_element = driver.find_element(By.ID, "mySelect")
# select_object = Select(select_element)
# select_object.select_by_value("75%")
#
#
# checkbox1 = driver.find_element(By.CLASS_NAME, "checkBoxClassA")
# checkbox1.click()
#
# draggable = driver.find_element(By.ID, "logo")
# target = driver.find_element(By.ID, "drop2")
# actions.click_and_hold(draggable).move_to_element(target).release().perform()
#
# linkName = driver.find_element(By.NAME, "linkName1")
# print(linkName.get_attribute("href"))
#
# clickMeButton = driver.find_element(By.ID, "myButton")
# for _ in range(5):
#     clickMeButton.click()
#     sleep(0.5)
#
# radioButton = driver.find_element(By.ID, "radioButton2")
# radioButton.click()


# RANDEVU SİSTEMİ ÖRNEĞİ
#driver.get("https://randevu.nvi.gov.tr/")
# surucuBelgesiJS = "setVal('appointmentType', 2);"
# driver.execute_script(surucuBelgesiJS)
#
# kabulButonu = "//button[contains(text(), 'Kabul Ediyorum')]"
# wait.until(EC.element_to_be_clickable((By.XPATH, kabulButonu))).click()
#
# adBilgisi = driver.find_element(By.CSS_SELECTOR, '[data-name="FirstName"]')
# adBilgisi.send_keys("güney")
#
# soyadBilgisi = driver.find_element(By.CSS_SELECTOR, '[data-name="LastName"]')
# soyadBilgisi.send_keys("bircan")
#
# kimlikBilgisi = driver.find_element(By.CSS_SELECTOR, '[data-name="IdentityNo"]')
# kimlikBilgisi.send_keys("274563634646")
#
# gunBilgisi = driver.find_element(By.CSS_SELECTOR, '[data-name="BirthDay"]')
# gunBilgisi.send_keys("10")
#
# ayBilgisi = driver.find_element(By.CSS_SELECTOR, '[data-name="BirthMonth"]')
# ayBilgisi.send_keys("3")
#
# yilBilgisi = driver.find_element(By.CSS_SELECTOR, '[data-name="BirthYear"]')
# yilBilgisi.send_keys("2004")
#
# mobilePhone = driver.find_element(By.CSS_SELECTOR, '[data-name="MobilePhone"]')
# mobilePhone.send_keys("5353 53 53")
#
# gondermeButonu = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
# gondermeButonu.click()

sleep(3000)
