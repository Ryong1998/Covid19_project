# 연도 및 달별 인구 구조 저장을 위한 코드
import warnings
warnings.filterwarnings('ignore')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select # 드롭다운 선택을 위햇 ㅓ임포트
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromeOptions = webdriver.ChromeOptions() # 크롬 드라이버 옵션 설정
chromeOptions.add_argument("--profile-directory=AutoUser")
prefs = {"download.default_directory" : "C:\self_project\covid_project\covid19_project\dataset"} # 파일다운로드 경로 설정
chromeOptions.add_experimental_option("prefs",prefs) # 옵션 정의

chromedriver = 'C:/Users/LG/dev_python/Webdriver/chromedriver.exe' # 윈도우 
driver_chrome = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions) # 설정 반영

# 크롤링할 사이트 호출
driver_chrome.get("https://jumin.mois.go.kr/ageStatMonth.do") # 셀리니움으로 크롤링할 메인 페이지 이동
time.sleep(1)



# csv 다운로드 까지 됨 - 근데 다운로드 하고 중지가 됨, 크롬 다운로드 상태바 안나오게 하는 설정 필요!
download_btn = driver_chrome.find_element_by_id('csvDown') # 검색 태그 선택
download_btn.click() # 태그 클릭
time.sleep(2)
driver_chrome.switch_to.alert.accept() #엔터키입력을 통해 다운로드 진행
time.sleep(5)

district_city = driver_chrome.find_element_by_name("sltOrgLvl1") #행정구역 시 태그 선택
district_city_dropdown = Select(district_city) # 드롭다운 선택을 위해서 Select 함수 이용
district_city_dropdown.select_by_index('1') #행정구역 시 상세선택
time.sleep(1)

driver_chrome.close()