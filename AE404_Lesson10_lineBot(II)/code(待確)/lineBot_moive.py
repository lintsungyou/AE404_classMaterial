from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
import requests
from bs4 import BeautifulSoup
line_bot_api = LineBotApi('your TOKEN')
UserID = 'your UserID'

response = requests.get('https://movies.yahoo.com.tw/movie_thisweek.html')
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all('div', class_ = 'release_info_text')

for index, info in enumerate(data[:10]):
    movie_name = info.find('div', class_ = 'release_movie_name').find('a').text
    movie_name = movie_name.strip()

    try:
        trailerUrl = soup.find_all('div',class_='release_btn color_btnbox')[index].find_all('a')[1]['href']
    except:
        trailerUrl = 'Yahoo電影沒有這部的預告片喔!'

    imgSrc = soup.find_all('div',class_='release_foto')[index].find('img')['data-src']
    temp = [movie_name, trailerUrl, imgSrc]

    movie = '電影資訊：' + movie_name + '\n預告片：' + trailerUrl
    line_bot_api.push_message(UserID, TextSendMessage(text = movie))

    image_message = ImageSendMessage(
        original_content_url = imgSrc,
        preview_image_url = imgSrc)
    line_bot_api.push_message(UserID, image_message)
