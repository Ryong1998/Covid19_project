# 연도 및 달별 인구 구조 저장을 위한 코드(셀레니움)
import warnings
warnings.filterwarnings('ignore')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select # 드롭다운 선택을 위햇 ㅓ임포트
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromeOptions = webdriver.ChromeOptions() # 크롬 드라이버 옵션 설정
prefs = {"download.default_directory" : "C:/self_project/covid_project/covid19_project/dataset/real_estate"} # 파일다운로드 경로 설정
chromeOptions.add_experimental_option("prefs",prefs) # 옵션 정의

chromedriver = 'C:/Users/LG/dev_python/Webdriver/chromedriver.exe' # 윈도우 
driver_chrome = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions) # 설정 반영

# 크롤링할 사이트 호출
driver_chrome.get("https://data.kbland.kr/kbstats/investment-table") # 셀리니움으로 크롤링할 메인 페이지 이동
time.sleep(3)


# driver_chrome.quit() -
driver_chrome.quit()