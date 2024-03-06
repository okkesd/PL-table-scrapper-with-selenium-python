from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://rivalregions.com/")
time.sleep(5)
driver.maximize_window()
e_mail = "donbalogluali07@mail.com"
sifre = "12122004"


driver.find_element(by="xpath",value='//div[@class="sa_radius"]/div[@style="margin-left: 200px;"]/a[@class="sa_link"]/div').click()
time.sleep(5)

driver.find_element(by="xpath",value='//div[@class="clearfix _5466 _44mg"][1]/input').send_keys(e_mail)
driver.find_element(by="xpath",value='//div[@class="clearfix _5466 _44mg"][2]/input').send_keys(sifre)
time.sleep(5)
driver.find_element(by="xpath",value='//div[@class="_xkt"]/button').click() #giriş butonu
time.sleep(10)
try:
    driver.find_element(by="xpath",value='//div[@class="clearfix _5466 _44mg"][2]/input').send_keys(sifre)
    driver.find_element(by="xpath",value='//button[@class="_42ft _4jy0 _52e0 _4jy6 _4jy1 selected _51sy"]').click()  ##giriş butonu
    time.sleep(10)
except:
    driver.find_element(by="xpath",value='//div[@action="storage"]').click() #depoya gir butonu
    time.sleep(10)
title = driver.current_url
if(title=='https://rivalregions.com/#storage'):
    driver.find_element(by="xpath",value='//div[@url="26"]').click()  # rv ye tıkla butonu
    time.sleep(10)
else:
    driver.find_element(by="xpath", value='//div[@action="storage"]').click() #depoya gir butonu
    time.sleep(10)
    driver.find_element(by="xpath",value='//div[@url="26"]/div').click() # rv ye gir butonu
    time.sleep(10)

i=0
while True:
    isim = driver.find_element(by="xpath",value='//div[@class="storage_whose float_left small"]/span[2]').text # o anda kimin satış yaptığının isminin butonu
    if(isim=="Polat Alemdar"):
        time.sleep(350)
    else:
        mevcut= driver.find_element(by="xpath",value='//span[@class="storage_see pointer tip hov2 imp"]/span').text  # marketteki fiyatı alma
        mevcut=mevcut[:-2]
        mevcut=mevcut.replace(".","")
        mevcut=int(mevcut)
        print("parayı çektik")
        if(mevcut>70000):
            teklif_check = driver.find_element(by="xpath",value='//div[@class="float_left small"]/span') # teklifi yerleştir veya teklifi değiştir mi olduğunu anlamak için text alır
            if(teklif_check=='teklif yerleştir'):
                driver.find_element(by="xpath",value='//div[@class="float_left small"]/span').click()  # teklif yerleştirme sayfasına ulaşma butonu
                time.sleep(10)
                driver.find_element(by="xpath",value='//div[@class="float_left storage_sell_ammount_2"]/input').send_keys(mevcut-1)  # satış fiyatını yazıdırır
                time.sleep(3)
                driver.find_element(by="xpath",value='//span[@class="storage_buy_button_inner"]').click()  # satışa koyma butonuna tıklar
                time.sleep(350)
                driver.refresh()
                driver.find_element(by="xpath", value='//div[@url="26"]/div').click() # yeniledikten sonra tekrar rv kısmına tıklar
                time.sleep(5)
            else:
                driver.find_element(by="xpath", value='//div[@class="float_left small"]/span').click() # teklif yerleştirme sayfasına ulaşma butonu
                time.sleep(10)
                metin = str(mevcut)
                driver.find_element(by="xpath", value='//div[@class="float_left storage_sell_ammount_2"]/input').send_keys(Keys.BACKSPACE * len(metin)) # olan teklif fiatını siler
                time.sleep(5)
                driver.find_element(by="xpath", value='//div[@class="float_left storage_sell_ammount_2"]/input').send_keys(mevcut - 1)  # satış fiyatını yazıdırır
                driver.find_element(by="xpath", value='//span[@class="storage_buy_button_inner"]').click()  # satışa koyma butonuna tıklar
                time.sleep(350)
                driver.refresh()
                time.sleep(3)
                driver.find_element(by="xpath", value='//div[@url="26"]/div').click()  # yeniledikten sonra tekrar rv kısmına tıklar
                time.sleep(4)
        else:
            time.sleep(350)
            driver.refresh()
            driver.find_element(by="xpath", value='//div[@url="26"]/div').click()
            time.sleep(5)
