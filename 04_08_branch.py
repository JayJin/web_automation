import requests
from bs4 import BeautifulSoup

# 여기에 코드를 작성하세요
response = requests.get("https://workey.codeit.kr/orangebottle/index")
orange_page = response.text

soup = BeautifulSoup(orange_page, 'html.parser')

branch_infos = []
branch_tags = soup.select('.branch .city, .branch .address, .branch .phoneNum')

for i in range(int(len(branch_tags)/3)):
    branch_infos.append([branch_tags[3*i].get_text(), branch_tags[3*i+1].get_text(), branch_tags[3*i+2].get_text()])


# 테스트 코드
print(branch_infos)