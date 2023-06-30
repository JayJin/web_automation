# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://workey.codeit.kr/music')
# music_page = response.text

# soup = BeautifulSoup(music_page, 'html.parser')

# popular_artists = []

# for tag in soup.select('ul.polular__order li'):
#     popular_artists.append(tag.get_text().strip())

# print(popular_artists)



# 위의 BeautifulSoup 코드를 Selenium 코드로 변환



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)


# 사이트 접속하기
driver.get('https://workey.codeit.kr/music')

# 웹 페이지가 로딩될 때 까지 기다려주기
# driver.implicitly_wait(3)
time.sleep(1)

popular_artists = []

for artist in driver.find_elements(By.CSS_SELECTOR, 'ul.popular__order li'):
    popular_artists.append(artist.text.strip())
# 로그인하기 (1)

print(popular_artists)