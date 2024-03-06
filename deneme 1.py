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
    driver.get('https://rivalregions.com/#slide/profile/868625164333238')
    time.sleep(5)
    ben = driver.find_element(by="xpath",value='//h1[@class="white hide_for_name"]').text
    ben = ben[9:]
except:
    driver.get('https://rivalregions.com/#slide/profile/868625164333238')
    time.sleep(3)
    driver.refresh()
    time.sleep(5)
    ben = driver.find_element(by="xpath", value='//h1[@class="white hide_for_name"]').text
    ben = ben[9:]
driver.get('https://rivalregions.com/#auction/all')

time.sleep(10)
driver.refresh()
time.sleep(3)
driver.find_element(by="xpath",value='//tr[3]/td[@class="list_level"][3]/div').click()  #bahise gir butonu
time.sleep(5)

i=1
for i in range (0,100):
    time.sleep(5)
    para= driver.find_element(by="xpath",value='//div[@class="tip imp white"]/span').text  # olan parabutonu
    para= para.replace(".","")
    para=int(para)
    if(para<440000000000):
        kalan_süre=driver.find_element(by="xpath", value='//h4[@class="white margin hasCountdown"]').text # kalan süreyi alır
        if(kalan_süre=="00:00"):
            giden = driver.find_element(by="xpath", value='//div[@class="small tc hov2 pointer"]/span').text
            print(giden)
            driver.quit()
        else:
            check = driver.find_element(by="xpath", value='//div[@class="small tc hov2 pointer"]/span').text  # olan ismi bulma butonu
            if (ben == check):
                time.sleep(12)
                driver.refresh()
                time.sleep(3)
            else:

                time.sleep(5)
                driver.find_element(by="xpath",value='//div[@class="imp button_blue auction_plus"][1]').click()  # artırma butonu
                driver.find_element(by="xpath",value='//div[@class="button_green"]').click()  # ihaleye bas butonu
                time.sleep(15)
                driver.refresh()


        i=i+1
    else:
        giden = driver.find_element(by="xpath", value='//div[@class="small tc hov2 pointer"]/span').text
        print(giden)
        break
