from selenium import webdriver
import time


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
driver.find_element(by="xpath",value='//div[@class="_xkt"]/button').click()
time.sleep(10)
try:
    driver.find_element(by="xpath",value='//div[@class="clearfix _5466 _44mg"][2]/input').send_keys(sifre)
    driver.find_element(by="xpath",value='//button[@class="_42ft _4jy0 _52e0 _4jy6 _4jy1 selected _51sy"]').click()
    time.sleep(10)
    driver.find_element(by="xpath", value='//div[@class="_xkt"]/button').click()
    time.sleep(10)
    driver.get('https://rivalregions.com/#listed/state_population/4106')
    driver.refresh()

except:
    driver.get('https://rivalregions.com/#listed/state_population/4106')
    driver.refresh()
time.sleep(5)
i = 6
driver.maximize_window()
time.sleep(3)
while (i<26) :
    values = "//tbody/tr[" + str(i) + "]/td"
    print(values)
    driver.find_element(by="xpath", value=values).click()
    time.sleep(5)
    driver.find_element(by="xpath", value='//div[@id="slide_profile_send_message"]').click()
    time.sleep(3)
    message = "Join AOG state tg group for taking information about where the best ore and diamond factories are :           https://t.me/AogState"
    driver.find_element(by="xpath", value='//textarea').send_keys(message)
    time.sleep(3)
    driver.find_element(by="xpath", value='//button[@class="button_blue emojied_send"]').click()
    time.sleep(3)
    driver.get("https://rivalregions.com/#listed/state_population/4106")
    time.sleep(3)
    driver.refresh()
    time.sleep(5)
    i = i+1
driver.quit()
