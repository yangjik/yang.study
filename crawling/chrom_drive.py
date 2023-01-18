# crawling : selenium

# pip install chromedriver-autoinstaller
# 설치하는 이유
# 라이브러리 사용안하면 크롬버전이 바뀌면 실행안됨.
# 그러면 매번 직접 크롬버전확인하고 크롬드라이버 exe파일 받아야되는 문제생김

import selenium
from selenium import webdriver
import chromedriver_autoinstaller
import os
import time

# 크롬 버전 get
chrome_version = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_version}/chromedriver.exe'

if os.path.exists(driver_path):
    # print('크롬 드라이버 이미 존재합니다.\n경로는 : ', driver_path)
    pass
else:
    # print(f'크롬 드라이버 설치\n(ver : {chrome_version})')
    chromedriver_autoinstaller.install(True)

driver = webdriver.Chrome(driver_path)
# 네이버 항공편
driver.get('https://flight.naver.com/')
time.sleep(2)

driver.find_element_by_css_selector('#__next > div > div.container.as_main > div.popup_travelclub > div > div.btns > button:nth-child(2)').click()
time.sleep(2)

driver.find_element_by_css_selector('#__next > div > div.container.as_main > div.main_searchbox__3vrV3 > div > div > div.searchBox_tabpanel__1BSGR > div.tabContent_routes__laamB > button.tabContent_route__1GI8F.select_City__2NOOZ.end > i').click()
time.sleep(2)

# insert_from = str(input('도착지를 입력하세요. '))
box = driver.find_element_by_css_selector('#__next > div > div.container.as_main > div.autocomplete_autocomplete__ZEwU_.autocomplete_is_arrival__JR22W > div.autocomplete_header__1NSMD > div > input')
time.sleep(2)

box.send_keys('후쿠오카')
# box.send_keys(insert_from)
time.sleep(2)

driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a/div').click()
time.sleep(2)


driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()