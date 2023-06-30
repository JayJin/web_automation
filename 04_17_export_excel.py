import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

wb = Workbook(write_only=True)      # write_only : 데이터를 사용만 한다
ws = wb.create_sheet('TV Ratings')      # 워크시트 만들기

ws.append(['순위', '채널', '프로그램', '시청률'])

response = requests.get(" https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(),      # 순위
        td_tags[1].get_text(),      # 채널
        td_tags[2].get_text(),      # 프로그램
        td_tags[3].get_text(),      # 시청률
    ]
    ws.append(row)

wb.save('시청률_2010년1월1주차.xlsx')