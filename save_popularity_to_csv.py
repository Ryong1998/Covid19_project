# 연도 및 달별 인구 구조 저장을 위한 코드
import warnings
warnings.filterwarnings('ignore')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/Users/LG/dev_python/Webdriver/chromedriver.exe' # 윈도우 
#chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)

# 크롤링할 사이트 호출
driver.get("https://jumin.mois.go.kr/ageStatMonth.do")
time.sleep(2)
driver.quit()