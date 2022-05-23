# 오픈 api 이용해서 코로나 기본 데이터들 가져오는 코드

import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용

enddate = "20220131" # 2022년 1월 31일 이후로 누적검사자 수가 없다, 그래서 마지막 날짜를 2022년1월31일로 설정
startdate="20200120"

service_key = 'OtlfaJxmWNmyxJI3MPVTRTrJKBOe7Qks7%2FTcHRZscnpf2e%2B4oKSbfzCMhU4RewP3729MnEvUD0pJgzJ8DIh3VQ%3D%3D' #키입력
params = "&numOfRows=10&pageNo=1&startCreateDt="+startdate+"&endCreateDt="+enddate+"'" #요청변수 입력
open_api = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?ServiceKey=' + service_key + params #사이트 키입력 입력변수 조합

res = requests.get(open_api) #공공데이터는 네이버와 달리 headers 사용안하고 붙여서 쓰게 해놓는다


#xml 파일 형식이므로 파싱과정 필요
soup = BeautifulSoup(res.content, 'html.parser')

# 공공api를 이용해서 받아올 정보들을 담을 리스트
stateDt_list = list() # 기준날짜 리스트
decideCnt_list = list() # 누적 확진자수 리스트
accExamCnt_list = list() # 누적 검사자수 리스트
deathCnt_list = list() # 누적 사망자수 리스트
daily_decideCnt_list = list() # 일일 확진자수 리스트
daily_accExamCnt_list = list() # 일일 검사자 수 리스트
daily_deathCnt_list = list() # 일일 사망자수 리스트

#원하는 정보의 (상위)태그들을 선택
items = soup.select('item') 

#  각 (상위)태그 들을 반복해서 안에 있는 하위 태그들의 정보들을 받아옴
for item in items:
    stateDt=item.select_one('stateDt') # 기준일을 태그로 받음
    stateDt_list.append(stateDt.get_text()) # 기준날짜 리스트에 하나씩 추가
    decideCnt=item.select_one('decideCnt') # 누적확진자 수를 태그로 받음
    decideCnt_list.append(int(decideCnt.get_text())) # 누적 확진자수 리스트에 하나씩 추가
    accExamCnt=item.select_one('accExamCnt') # 누적 검사자 수를 태그로 받음
    accExamCnt_list.append(int(accExamCnt.get_text())) # 누적 검사자수 리스트에 하나씩 추가
    deathCnt=item.select_one('deathCnt') # 누적사망자 수를 태그로 받음
    deathCnt_list.append(int(deathCnt.get_text())) # 누적 사망자수 리스트에 하나씩 추가
    
# 일일 확진자수,검사자수,사망자수 계산
# api로 받아올 때, 최근날짜가 먼저 나옴
for data in range(len(stateDt_list)-1):
    daily_decideCnt_list.append(decideCnt_list[data]-decideCnt_list[data+1]) # 일일 확진자수 리스트 생성(최근날짜-전날날짜)
    daily_accExamCnt_list.append(accExamCnt_list[data]-accExamCnt_list[data+1]) #일일 검사자수 리스트 생성
    daily_deathCnt_list.append(deathCnt_list[data]-deathCnt_list[data+1]) # 일일 사망자수 리스트 생성
daily_decideCnt_list.append(decideCnt_list[len(stateDt_list)-1]) # 측정 시작한 최초의 일일 확진자수를 해당 리스트에 추가
daily_accExamCnt_list.append(accExamCnt_list[len(stateDt_list)-1]) # 측정 시작한 최초의 검사자수를 해당 리스트에 추가
daily_deathCnt_list.append(deathCnt_list[len(stateDt_list)-1]) # 측정 시작한 최초의 사망자수를 해당 리스트에 추가


# 정보들을 담을 리스트를 확인하기 위한 출력
# print(stateDt_list)
# print(decideCnt_list)
# print(accExamCnt_list)
# print(deathCnt_list)



#누적 지표, 일일 지표들 관련 데이터 프레임 생성 한 후 정보들을 담은 리스트를 삽입
df = pd.DataFrame({
    "기준날짜" : stateDt_list,
    "누적확진자수" : decideCnt_list,
    "누적검사자수" : accExamCnt_list,
    "누적사망자수" : deathCnt_list,
    "일일확진자수" : daily_decideCnt_list,
    "일일검사자수" : daily_accExamCnt_list,
    "일일사망자수" : daily_deathCnt_list
    }
    
)
# 데이터 프레임의 인덱스를 설정
df=df.set_index("기준날짜")

# 인덱스를 날짜 순으로 정렬
df=df.sort_index(axis = 0)

# 데이터프레임을 csv파일로 저장
df.to_csv('covid19_project/dataset/covid_base/covid_base_data_1.csv', encoding='utf-8')

# tabulate을 통해 데이터프레임을 좀 더 예쁘게 출력
print(tabulate(df, headers='keys', tablefmt='psql'))