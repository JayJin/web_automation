import requests

# 웹 페이지 가져오기
# response = requests.get("https://workey.codeit.kr/ratings/index")
# rating_page = response.text

# print(rating_page)

#####################################################################
rating_pages = []

#https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
for i in range(5):
    url = f"https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={i}"
    response = requests.get(url)
    rating_page = response.text
    rating_pages.append(rating_page)

print(len(rating_pages))
print(rating_pages[0])