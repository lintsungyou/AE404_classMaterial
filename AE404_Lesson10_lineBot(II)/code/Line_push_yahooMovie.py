from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage
import requests
from bs4 import BeautifulSoup

line_bot_api=LineBotApi('Your_Channel_Access_Token')
UserID='Your_UserID'
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")

#取得yahoo本周新片10部
for movie in range(10):
    name = soup.find_all('div',class_='release_movie_name')[movie].find('a').text.strip()
    try:
        trailerUrl = soup.find_all('div',class_='release_btn color_btnbox')[movie].find_all('a')[1]['href']
    except:
        trailerUrl = 'Yahoo電影沒有這部的預告片喔!'
    imgSrc = soup.find_all('div',class_='release_foto')[movie].find('img')['src']

    text_message=TextSendMessage(text= '電影名稱: '+name+'\r\n預告片: '+trailerUrl)
    image_message = ImageSendMessage(
        original_content_url=imgSrc,
        preview_image_url=imgSrc
    )
    message = [text_message,image_message]
    line_bot_api.push_message(UserID,message)


