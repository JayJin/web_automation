import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music/index")
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

rank_tags = soup.select(".rank li")
popular_searches = []

for tag in rank_tags:
    popular_searches.append(list(tag.stripped_strings)[2])

print(popular_searches)