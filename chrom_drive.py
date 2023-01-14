# crawling : selenium

# pip install chromedriver-autoinstaller
# 설치하는 이유
# 라이브러리 사용안하면 크롬버전이 바뀌면 실행안됨.
# 그러면 매번 직접 크롬버전확인하고 크롬드라이버 exe파일 받아야되는 문제생김

import selenium
from selenium import webdriver
import chromedriver_autoinstaller
import os

# 크롬 버전 get
chrome_version = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_version}/chromedriver.exe'

if os.path.exists(driver_path):
    print('크롬 드라이버 이미 존재합니다.\n경로는 : ', driver_path)

else:
    print(f'크롬 드라이버 설치\n(ver : {chrome_version})')
    chromedriver_autoinstaller.install(True)

driver = webdriver.Chrome(driver_path)
driver.get('https://google.com')
