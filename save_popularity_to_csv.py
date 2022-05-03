# 연도 및 달별 인구 구조 저장을 위한 코드
import warnings
warnings.filterwarnings('ignore')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select # 드롭다운 선택을 위햇 ㅓ임포트
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/Users/LG/dev_python/Webdriver/chromedriver.exe' # 윈도우 
driver_chrome = webdriver.Chrome(chromedriver)

driver_firefox=webdriver.Firefox() # Firefox 다운받아야 할듯

# 크롤링할 사이트 호출
driver_chrome.get("https://jumin.mois.go.kr/ageStatMonth.do")
time.sleep(2)

elem = driver_chrome.find_element_by_id('sltOrgLvl1')
elem.send_keys(Keys.RETURN)
time.sleep(2)




# driver_firefox.quit()
driver_chrome.quit()