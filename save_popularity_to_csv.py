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
chromeOptions.add_experimental_option("prefs",prefs) # 옵션 정의

chromedriver = 'C:/Users/LG/dev_python/Webdriver/chromedriver.exe' # 윈도우 
driver_chrome = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions) # 설정 반영

# 크롤링할 사이트 호출
driver_chrome.get("https://jumin.mois.go.kr/ageStatMonth.do") # 셀리니움으로 크롤링할 메인 페이지 이동
time.sleep(1)

lst_2020 = ['03','04','05','06','07','08','09','10','11','12'] # 2020년의 해당 월들을 리스트로 생성
lst_2021 = ['01','02','03','04','05','06','07','08','09','10','11','12'] # 2021년의 해당 월들을 리스트로 생성


def click_download_button(tag):
    download_btn = driver_chrome.find_element_by_id(tag) # 검색 태그 선택
    download_btn.click() # 태그 클릭
    time.sleep(2)
    driver_chrome.switch_to.alert.accept() # 알람 확인을 통해 다운로드 진행
    time.sleep(5)
    

# 행정구역 시 들 리스트화
district_city = driver_chrome.find_element_by_name("sltOrgLvl1") #행정구역 시 태크 선택
city_list=list(district_city.text.split("\n")) # 엔터 기준으로 문자열 나눔
city_list.remove(' ') # " "인 요소 제거
print(city_list) # 행정구역 시 들 리스트 확인위해 출력

for city_index in range(len(city_list)): # 인덱스로 행정구역 모든 시 들에 접근하기 위해서 반복문 사용 
    
    
    district_city = driver_chrome.find_element_by_name("sltOrgLvl1") #행정구역 시 태그 선택
    district_city_dropdown = Select(district_city) # 드롭다운 선택을 위해서 Select 함수 이용
    district_city_dropdown.select_by_index(str(city_index)) #행정구역 시 상세선택
    time.sleep(1)


    # 행정구역 구 들 리스트화
    district_gu = driver_chrome.find_element_by_name("sltOrgLvl2") #행정구역 구 창 선택
    gu_list=list(district_gu.text.split("\n")) # 엔터 기준으로 문자열 나눔
    if ' ' in gu_list:  # " " 가 리스트에 있으면
        gu_list.remove(' ') # " "인 요소 제거
    print(gu_list) # 행정구역 구 들 리스트 확인위해 출력

    
    for gu_index in range(len(gu_list)): # 인덱스로 행정구역 모든 구 들에 접근하기 위해서 반복문 사용 
        district_gu = driver_chrome.find_element_by_name("sltOrgLvl2") #행정구역 구 태그 선택
        district_gu_dropdown = Select(district_gu) # 드롭다운 선택을 위해서 Select 함수 이용
        district_gu_dropdown.select_by_index(str(gu_index)) #행정구역 구 상세선택
        time.sleep(1)
        
        for year in range(2020,2022): #2020년 2022년 년도 반복

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

            year_list=list()
            if year == 2020: # 2020년이면
                year_list=lst_2020 # 2020년의 월 리스트를 사용
            elif year == 2021: # 2021년이면 
                year_list=lst_2021 # 2021년의 월 리스트를 사용
                
            for month_value in year_list: # 선택한 년의 리스트 요소인 월을 사용
                # 시작날짜 달 선택
                startmonth = driver_chrome.find_element_by_name("searchMonthStart") 
                startmonth_dropdown = Select(startmonth)
                startmonth_dropdown.select_by_value(str(month_value))
                time.sleep(1)

            
                # 끝날짜 달 선택
                endmonth = driver_chrome.find_element_by_name("searchMonthEnd") 
                endmonth_dropdown = Select(endmonth)
                endmonth_dropdown.select_by_value(str(month_value))
                time.sleep(1)

                # 검색선택
                search_btn = driver_chrome.find_element_by_class_name("btn_search") # 검색 태그 선택
                search_btn.click() # 태그 클릭
                time.sleep(2)

               
                click_download_button('csvDown')
        




# driver_chrome.quit() -
driver_chrome.quit()