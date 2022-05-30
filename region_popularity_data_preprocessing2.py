# 파일들을 성별로, 나이대별, 지역별로 나누어서 저장 -> ver2
# 파일명 : 지역_성별_나이대       /   인덱스 : 시간 컬럼으로 년 월 구분해서 생성하기  컬럼: 상세지역들

import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
import os

# path_dir = 'C://self_project//covid_project//covid19_project//dataset//region_popularity'
# file_lists = os.listdir(path_dir)

df = pd.read_csv("C://self_project//covid_project//covid19_project//dataset//region_popularity_ver2//강원도.csv",  encoding='utf-8') # 추후 수정 필요

for i in range(len(df['카테고리'])):
    if df['카테고리'][i].split("_")[1] =="남" and df['카테고리'][i].split("_")[2] =="10~19세":
        print(i)
        print(df['카테고리'][i])
        print(df.iloc[i])
        print()
        

# print(df[df['카테고리']=='2021년12월_여_60~69세'])

