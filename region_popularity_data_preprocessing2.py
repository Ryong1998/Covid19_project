# 파일들을 성별로, 나이대별, 지역별로 나누어서 저장 -> ver2
# 파일명 : 지역_성별_나이대       /   인덱스 : 시간 컬럼으로 년 월 구분해서 생성하기  컬럼: 상세지역들

import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
import os


def func(df_data):
    df_data = df_data.split('_')[0]   
    return df_data


# path_dir = 'C://self_project//covid_project//covid19_project//dataset//region_popularity'
# file_lists = os.listdir(path_dir)

# 임시 테스트를 위해서 파이 하나 만을 읽음
df = pd.read_csv("C://self_project//covid_project//covid19_project//dataset//region_popularity_ver2//강원도.csv",  encoding='utf-8') # 추후 수정 필요

# 년도와 월을 컬럼으로 추가
df['년월'] = df['카테고리'].str.split('_',expand=True)[0]
df['년도'] = df['년월'].str.split('년',expand=True)[0]
df['월'] = df['년월'].str.split('년',expand=True)[1].str.split('월',expand=True)[0]

# 성별을 컬럼을 추가
df['성별'] = df['카테고리'].str.split('_',expand=True)[1]

# 나이를 컬럼으로 추가
df['나이'] = df['카테고리'].str.split('_',expand=True)[2]

print(df.info())

df.head()