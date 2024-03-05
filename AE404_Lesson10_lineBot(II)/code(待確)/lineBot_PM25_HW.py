import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
from selenium.webdriver.common.by import By
line_bot_api = LineBotApi('your TOKEN')
UserID = 'your UserID'

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


chrome = webdriver.Chrome()
chrome.get('https://airtw.epa.gov.tw/')

select = Select(chrome.find_element(By.ID, 'ddl_county'))
select.select_by_index(1)
time.sleep(2)

date = chrome.find_element(By.CLASS_NAME, 'date')
info = date.text
info = info.split('\n')

time = info[0]
location = info[1]


airinfo = chrome.find_element(By.ID, 'aqicircle')
airinfo = airinfo.text
airinfo = airinfo.split('\n')

PM25 = airinfo[1]
condition = airinfo[2]
quality = condition + ' PM2.5 = ' + PM25

chrome.close()

text_message = TextSendMessage(text = time + '\n' + location + '\n' + quality)
line_bot_api.push_message(UserID, text_message)


