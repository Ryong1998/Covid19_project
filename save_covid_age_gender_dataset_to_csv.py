import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용


#print(enddate)
enddate = "20220131" # 2022년 1월 31일 이후로 누적검사자 수가 없다, 그래서 마지막 날짜를 2022년1월31일로 설정
startdate="20200120"



service_key = 'OtlfaJxmWNmyxJI3MPVTRTrJKBOe7Qks7%2FTcHRZscnpf2e%2B4oKSbfzCMhU4RewP3729MnEvUD0pJgzJ8DIh3VQ%3D%3D' #키입력
params = "&numOfRows=10&pageNo=1&startCreateDt="+startdate+"&endCreateDt="+enddate+"'" #요청변수 입력
open_api = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson?ServiceKey=' + service_key + params #사이트 키입력 입력변수 조합

res = requests.get(open_api) #공공데이터는 네이버와 달리 headers 사용안하고 붙여서 쓰게 해놓는다


#xml 파일 형식이므로 파싱과정 필요
soup = BeautifulSoup(res.content, 'html.parser')

# 공공api를 이용해서 받아올 정보들을 담을 리스트
createDt_list = list() # 등록날짜 리스트
confCase_list = list() # 누적 해당 카데고리의 확진자수 리스트
death_list = list() # 누적 해당 카데고리의 사망자수 리스트
gubun_list = list() # 어느 카테고리에 속하는지 알려주는 리스트





#원하는 정보의 (상위)태그들을 선택
items = soup.select('item')
count=0

#  각 (상위)태그 들을 반복해서 안에 있는 하위 태그들의 정보들을 받아옴
for item in items:
    createDt=item.select_one('createDt') # 등록날짜을 태그로 받음
    createDt_list.append(createDt.get_text().split()[0])
    confCase=item.select_one('confCase') # 누적 해당 카데고리의 확진자수를 태그로 받음
    confCase_list.append(int(confCase.get_text()))
    death=item.select_one('death') # 누적 해당 카데고리의 사망자수를 태그로 받음
    death_list.append(int(death.get_text()))
    gubun=item.select_one('gubun') # 어느 카테고리에 속하는지를 태그로 받음
    gubun_list.append(gubun.get_text())

    
df = pd.DataFrame({
    "기준날짜" : createDt_list,
    "누적확진자수" : confCase_list,
    "누적사망자수" : death_list,
    "카테고리" : gubun_list
    
})

# 데이터 프레임의 인덱스를 설정
df=df.set_index("기준날짜")

# 인덱스를 날짜 순으로 정렬
df=df.sort_index(axis = 0)

# 데이터 프레임 중 카테고리 컬럼의 데이터값들의 종류 확인
print(df['카테고리'].unique())

# 카테고리 별로 데이터 프레임 복사해서 생성
df_0 = df[df['카테고리']=='0-9'].copy()
df_male = df[df['카테고리']=='남성'].copy()
df_female = df[df['카테고리']=='여성'].copy()
df_80 = df[df['카테고리']=='80 이상'].copy()
df_70 = df[df['카테고리']=='70-79'].copy()
df_10 = df[df['카테고리']=='10-19'].copy()
df_50 = df[df['카테고리']=='50-59'].copy()
df_40 = df[df['카테고리']=='40-49'].copy()
df_30 = df[df['카테고리']=='30-39'].copy()
df_20 = df[df['카테고리']=='20-29'].copy()
df_60 = df[df['카테고리']=='60-69'].copy()

# 카테고리 컬럼을 제외한 값들을 csv 파일로 저장
df_0[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_0.csv', encoding='utf-8')
df_10[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_10.csv', encoding='utf-8')
df_20[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_20.csv', encoding='utf-8')
df_30[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_30.csv', encoding='utf-8')
df_40[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_40.csv', encoding='utf-8')
df_50[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_50.csv', encoding='utf-8')
df_60[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_60.csv', encoding='utf-8')
df_70[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_70.csv', encoding='utf-8')
df_80[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_80.csv', encoding='utf-8')
df_male[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_male.csv', encoding='utf-8')
df_female[['누적확진자수','누적사망자수']].to_csv('covid19_project/dataset/covid_category_female.csv', encoding='utf-8')

# 데이터 프레임으로 의도한 대로 처리가 됬는 확인하기 위해서 출력
print(tabulate(df_0[['누적확진자수','누적사망자수']].head(), headers='keys', tablefmt='psql'))

