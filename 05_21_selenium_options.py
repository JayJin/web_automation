import requests
import time
import csv

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
from openpyxl import Workbook

# 크롬 드라이버 생성
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(0.5)

# 사이트 접속하기
driver.get('http://info.nec.go.kr/electioninfo/electionInfo_report.xhtml')
time.sleep(1)