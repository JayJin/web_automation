import time

from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_option)
driver.implicitly_wait(1)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)

# 로그인
login_link = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()
# visibility_of_element_located() : 웹 요소가 실제로 보일 때까지 기다리기
id_box = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')
pw_box = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')
login_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()

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
post_links = driver.find_elements(By.CSS_SELECTOR, 'div.post-list__post')
print(post_links)

for post_link in post_links:
    # 포스트 클릭
    post_link.click()
    time.sleep(1)

    # 이미지 주소 가져와서 출력하기
    style_attr = driver.find_element(By.CSS_SELECTOR, '.post-container__image').get_attribute('style')
    image_path = style_attr.split('"')[1]
    print(image_path)
    time.sleep(1)

    # 포스트 모달창 종료 버튼 클릭
    exit_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.close-btn')))
    exit_button.click()
    time.sleep(1)

driver.quit()
