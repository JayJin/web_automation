import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import csv

wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['기간', '순위', '프로그램', '시청률'])

# CSV 파일 생성
csv_file = open('SBS_데이터2.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['기간', '순위', '프로그램', '시청률'])

for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, weekIndex)
            response = requests.get(url)
            rating_page = response.text

            soup = BeautifulSoup(rating_page, "html.parser")

            for tr_tag in soup.select('.row')[1:]:
                tr_tags = tr_tag.select('td')
                period = "{}년 {}월 {}주차".format(year, month, weekIndex+1)
                if tr_tags[1].get_text() == 'SBS':
                    row = [
                        period,
                        tr_tags[0].get_text(),      # 순위
                        tr_tags[2].get_text(),      # 프로그램
                        tr_tags[3].get_text(),      # 시청률
                    ]
                    ws.append(row)
                    csv_writer.writerow(row)

csv_file.close()
wb.save('SBS_데이터2.xlsx')

            
