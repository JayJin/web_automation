# 05_13과 동일하나 Selenium + BeautifulSoup을 활용한 코드

import time
from selenium import webdriver
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

# 엑셀 파일 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet('플레이 리스트')
ws.append(['제목', '해시태그', '좋아요 수', '곡 수'])

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/music')
time.sleep(1)

# 페이지 끝까지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

### 스크롤 완료 ### 
music_page = driver.page_source
driver.quit()

soup = BeautifulSoup(music_page, 'html.parser')

playlists = soup.select('.playlist__meta')

for playlist in playlists:
    title = playlist.select_one('h3.title').get_text()
    hashtags = playlist.select_one('p.tags').get_text()
    like_count = playlist.select_one('span.data__like-count').get_text()
    music_count = playlist.select_one('span.data__music-count').get_text()
    ws.append([title, hashtags, like_count, music_count])

wb.save('./4. 웹 자동화/플레이리스트.xlsx')