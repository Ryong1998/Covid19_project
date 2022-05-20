# pandas 라이브러리 import

import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용


# csv 파일 읽기, 경로는 상대경로, 절대경로 중 선택해서 기입

df = pd.read_csv("C://self_project//covid_project//covid19_project//dataset//region_popularity//202112_202112_연령별인구현황_월간.csv", encoding='cp949')
df = df.set_index('행정구역') # 데이터프레임의 인덱스 설정


df = df.transpose() # 데이터 프레임의 컬럼들과 인덱스 설정(기존에는 인덱스가 지역, 컬럼이 연령별 카테고리 였는데 인덱스를 연령별 카테고리로, 컬럼을 지역으로 설정)
season=df.index[0].split("_")[0] # 0000년00월 을 변수에 담음

print(tabulate(df, headers='keys', tablefmt='psql'))
print("index!!!!")
print(df.index)
print("columns!!!!")
print(df.columns)
print()
print()
print(season)