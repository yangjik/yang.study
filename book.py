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

    total = soup.select_one("#Search3_Result")

    txt = open('./check.txt', 'w', encoding='utf-8')

    txt.writelines(total)

    txt.close()

    object = soup.select_one("#Search3_Result > div:nth-of-type(1) > table > tr > td:nth-of-type(3) > table > tr:nth-of-type(1) > td:nth-of-type(1) > div:nth-of-type(1) > ul > li:nth-of-type(2) > a > b")
    object = object.text

    price = soup.select_one("#Search3_Result > div:nth-of-type(1) > table > tr > td:nth-of-type(3) > table > tr:nth-of-type(1) > td:nth-of-type(1) > div:nth-of-type(1) > ul > li:nth-of-type(4) > span.ss_p2 >b > span ")

    price = price.text
    price = price.replace(",", "")
    print(total)

else:
    print('응답 코드 : ', state)