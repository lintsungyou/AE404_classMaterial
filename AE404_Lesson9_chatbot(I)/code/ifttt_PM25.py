import requests
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium import webdriver
chrome_options =Options()
chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://airtw.moenv.gov.tw/")
time.sleep(3)

#下拉選單選擇台北松山
selectCounty = Select(chrome.find_element(By.ID, 'ddl_county'))
selectCounty.select_by_index(1)
time.sleep(1)
selectSite = Select(chrome.find_element(By.ID, 'ddl_site'))
selectSite.select_by_index(4)
time.sleep(1)

#取得測站點、時間、PM2.5值
soup = BeautifulSoup(chrome.page_source,"html.parser")
air_info = soup.find_all('div',class_ = 'info')[0]
state = air_info.find('h4').text[:6]
date = air_info.find('div',class_ = 'date').text.strip()[:16]
PM25 = int(air_info.find('span',id = 'PM25').text)
air_quality = ''
if PM25<16:
    air_quality = "good"+' PM2.5 = '+str(PM25)
elif PM25<35:
    air_quality = "moderate"+' PM2.5 = '+str(PM25)
else:
    air_quality = "Unhealthy"+' PM2.5 = '+str(PM25)
webhook_key = "填入Webhook金鑰"
trigger_name = "填入觸發條件名稱"
url ='https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1={}&value2={}&value3={}'.format(date,state,air_quality)
#requests.get(url)
print(date,state,air_quality)