
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
driver.get('https://workey.codeit.kr/costagram/index')

# 웹 페이지가 로딩될 때 까지 기다려주기
# driver.implicitly_wait(3)
time.sleep(1)


# 로그인하기 (1)
# driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()        # 로그인 클릭
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,'.login-container__login-input').send_keys('codeit')        # 아이디 입력
# driver.find_element(By.CSS_SELECTOR,'.login-container__password-input').send_keys('datascience')        # 비밀번호 입력
# driver.find_element(By.CSS_SELECTOR,'.login-container__login-button').click()        # 로그인 버튼 클릭

# 로그인하기 (2)
# driver.find_element(By.CSS_SELECTOR,'#app > nav > div > a').click()        # 로그인 클릭
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > form > input.login-container__login-input').send_keys('codeit')        # 아이디 입력
# driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > form > input.login-container__password-input').send_keys('datascience')        # 비밀번호 입력
# driver.find_element(By.CSS_SELECTOR,'#app > div > div > div > form > input.login-container__login-button').click()        # 로그인 버튼 클릭

# 로그인하기 (3) - Explicit wait 사용
login_link = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

# visibility_of_element_located() : 웹 요소가 실제로 보일 때까지 기다리기
id_box = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')

pw_box = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input')))
pw_box.send_keys('datascience')

login_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button')))
login_button.click()

# driver.quit()