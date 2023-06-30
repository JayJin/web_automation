
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)


# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

# 웹 페이지가 로딩될 때 까지 기다려주기
# driver.implicitly_wait(3)
time.sleep(1)


# 로그인하기 (1)
# driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()        # 로그인 클릭
# driver.find_element(By.CSS_SELECTOR,'.login-container__login-input').send_keys('codeit')        # 아이디 입력
# driver.find_element(By.CSS_SELECTOR,'.login-container__password-input').send_keys('datascience')        # 비밀번호 입력
# driver.find_element(By.CSS_SELECTOR,'.login-container__login-button').click()        # 로그인 버튼 클릭

# 로그인하기 (2)
driver.find_element(By.CSS_SELECTOR,'#app > nav > div > a').click()        # 로그인 클릭
time.sleep(1)

driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > form > input.login-container__login-input').send_keys('codeit')        # 아이디 입력
driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > form > input.login-container__password-input').send_keys('datascience')        # 비밀번호 입력
driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > form > input.login-container__login-button').click()        # 로그인 버튼 클릭
