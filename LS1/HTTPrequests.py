# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:47:19 2020

@author: ShawnHou
"""

import requests
url = "https://www.books.com.tw"
data = requests.get(url)
#print(data)

print(data.text)