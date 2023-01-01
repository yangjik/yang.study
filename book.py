import requests
from bs4 import BeautifulSoup

# url 에 작가검색
word = input("작가명 입력해주세요 ")
# word = '베르나르베르베르'
# word = '기욤뮈소'
# word = '동백꽃필무렵'
url = f"https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=Book&SearchWord={word}"

# print(url)

# get방식으로 전송
res = requests.get(url)
state = res.status_code

# 응답코드
if state == 200:

    html = res.text
    soup = BeautifulSoup(html, "html.parser")

    # total = soup.select_one("#keyword_wrap > table > tr >td:nth-of-type(3) > div.ss_line5 > table > tr >td > div > span.ss_f_g_l ")

    # count =  int(total.text)

    # 25개만 조회
    for i  in range(1, 26):
        object = soup.select_one(f"#Search3_Result > div:nth-of-type({i}) > table > tr > td:nth-of-type(3) > table > tr:nth-of-type(1) > td:nth-of-type(1) > div:nth-of-type(1) > ul > li:nth-of-type(2) > a >b ")
 
        if object == None:
            # print("패스합니다")
            pass
        else:
            object = object.text
            price = soup.select_one(f"#Search3_Result > div:nth-of-type({i}) > table > tr > td:nth-of-type(3) > table > tr:nth-of-type(1) > td:nth-of-type(1) > div:nth-of-type(1) > ul > li:nth-of-type(4) > span.ss_p2 >b > span ")
            price = price.text
            price = price.replace(",", "")
  
            # 필요시 DB 여기서 저장

            print(object, " / ", price)

        i = i + 1

else:
    print('응답 코드 : ', state)