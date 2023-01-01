import requests
from bs4 import BeautifulSoup

word = '베르나르베르베르'
url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&SearchWord={word}"
# url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8"
print(url)

res = requests.get(url)
state = res.status_code


if state == 200:

    html = res.text
    soup = BeautifulSoup(html, "html.parser")

    re = soup.select("#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a > b")
#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a > b
    print(re)

else:
    print('응답 코드 : ', state)