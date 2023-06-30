import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')

# 로그인 링크 클릭
driver.find_element_by_css_selector('.top-nav__login-link').click()
time.sleep(1)

# 아이디 박스, 비밀번호 박스, 로그인 버튼 찾아놓기
id_box = driver.find_element_by_css_selector('.login-container__login-input')
pw_box = driver.find_element_by_css_selector('.login-container__password-input')
login_button = driver.find_element_by_css_selector('.login-container__login-button')

# 액션 실행

# 01 연결하는 방식
(ActionChains(driver)
    .send_keys_to_element(id_box, 'codeit')
    .send_keys_to_element(pw_box, 'datascience')
    .click(login_button)
    .perform())

# 02 나열하는 방식
actions = ActionChains(driver)
actions.send_keys_to_element(id_box, 'codeit')
actions.send_keys_to_element(pw_box, 'datascience')
actions.click(login_button)
actions.perform()

driver.quit()