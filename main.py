import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')
# print(soup.prettify())

# print(soup.select('title'))
program_title_tags = soup.select('td.program')

program_titles = []

for tag in program_title_tags:
    program_titles.append(tag.get_text())

# print(program_titles)


# 가장 위에 나타나는 하나만 가져오기 : select_one
print(soup.select_one('td.program'))