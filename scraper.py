from bs4 import BeautifulSoup
import requests
import re

link = 'https://vanillawowdb.com/?spells=7.8'

source = requests.get(link).text
soup = BeautifulSoup(source, 'lxml')

data = soup.find_all("script")

print(data)
