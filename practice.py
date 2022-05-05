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
prefs = {"download.default_directory" : "C:\self_project\covid_project\covid19_project\dataset"} # 파일다운로드 경로 설정
chromeOptions.add_experimental_option("prefs",prefs) # 옴션 정의

chromedriver = 'C:/Users/LG/dev_python/Webdriver/chromedriver.exe' # 윈도우 
driver_chrome = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions) # 설정 반영

# 크롤링할 사이트 호출
driver_chrome.get("https://jumin.mois.go.kr/ageStatMonth.do")
time.sleep(1)

lst_2020 = ['03','04','05','06','07','08','09','10','11','12']
lst_2021 = ['01','02','03','04','05','06','07','08','09','10','11','12']

# 행정구역 시 선택
district_city = driver_chrome.find_element_by_name("sltOrgLvl1") #행정구역 시 창 선택
# 행정구역 시들 리스트화
city_list=list(district_city.text.split("\n"))
city_list.remove(' ')
print(city_list)

for city_index in range(len(city_list)):
    district_city = driver_chrome.find_element_by_name("sltOrgLvl1") #행정구역 시 창 선택
    district_city_dropdown = Select(district_city)
    district_city_dropdown.select_by_index(str(city_index)) #행정구역 시 상세선택
    time.sleep(1)


    # 행정구역 구 선택
    district_gu = driver_chrome.find_element_by_name("sltOrgLvl2") #행정구역 구 창 선택
    gu_list=list(district_gu.text.split("\n"))
    if ' ' in gu_list:
        gu_list.remove(' ')
    print(gu_list)
    
    for gu_index in range(len(gu_list)):
        district_gu = driver_chrome.find_element_by_name("sltOrgLvl2") #행정구역 구 창 선택
        district_gu_dropdown = Select(district_gu)
        district_gu_dropdown.select_by_index(str(gu_index)) #행정구역 구 상세선택
        time.sleep(1)
        
        year=2021

        # 시작날짜 연도 선택
        startyear = driver_chrome.find_element_by_name("searchYearStart") 
        startyear_dropdown = Select(startyear)
        startyear_dropdown.select_by_value(str(year))
        time.sleep(1)
        
        # 끝날짜 연도 선택
        endyear = driver_chrome.find_element_by_name("searchYearEnd")
        endyear_dropdown = Select(endyear)
        endyear_dropdown.select_by_value(str(year))
        time.sleep(1)

        # 시작날짜 달 선택
        startmonth = driver_chrome.find_element_by_name("searchMonthStart") 
        startmonth_dropdown = Select(startmonth)
        startmonth_dropdown.select_by_value('12')
        time.sleep(1)

        
        # 끝날짜 달 선택
        endmonth = driver_chrome.find_element_by_name("searchMonthEnd") 
        endmonth_dropdown = Select(endmonth)
        endmonth_dropdown.select_by_value('12')
        time.sleep(1)

        # 검색선택
        search_btn = driver_chrome.find_element_by_class_name("btn_search")
        search_btn.click()
        time.sleep(2)

        




# driver_chrome.quit() -
driver_chrome.quit()