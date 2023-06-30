# import requests
# from bs4 import BeautifulSoup

# # HTML 코드 받아오기
# response = requests.get("https://workey.codeit.kr/orangebottle/index")

# # BeautifulSoup 사용해서 HTML 코드 정리
# soup = BeautifulSoup(response.text, 'html.parser')

# branch_infos = []

# # 모든 지점에 대한 태그 가져오기
# branch_tags = soup.select('div.branch')

# for branch_tag in branch_tags:
#     # 각 태그에서 지점 이름, 전화번호 가져오기
#     branch_name = branch_tag.select_one('p.city').get_text()
#     address = branch_tag.select_one('p.address').get_text()
#     phone_number = branch_tag.select_one('span.phoneNum').get_text()
#     branch_infos.append([branch_name, address, phone_number])

# # 테스트 코드
# print(branch_infos)



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
driver.get('https://workey.codeit.kr/orangebottle/index')
time.sleep(3)

branch_infos = []


for info in driver.find_elements(By.CSS_SELECTOR, 'div.container div'):
    city = info.find_element(By.CSS_SELECTOR, 'p.city').text.strip()
    address = info.find_element(By.CSS_SELECTOR, 'p.address').text.strip()
    pnum = info.find_element(By.CSS_SELECTOR, 'span.phoneNum').text.strip()
    branch_infos.append([city, address, pnum])

print(branch_infos)