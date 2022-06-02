# 전처리한 부동산원 데이터를 하나의 파일로 합치는 코드

# pandas 라이브러리 import

import pandas as pd
import os

get_path_dir = 'C://self_project//data_project//data_project_file//dataset//real_estate//부동산원_proprocessing1'
file_lists = os.listdir(get_path_dir)
df_dictionary = dict()
columns_count=0 # 개별 파일 별 컬럼의 개수들을 더해서 확인 위한 변수

# for문을 통해서 여러 데이터 프레임들 생성
for i,file_list in enumerate(file_lists):
    df_dictionary[i] = pd.read_csv(get_path_dir+"//"+file_list, encoding='utf-8') # 파일경로에 있는 csv 파일들을 가져와서 dict에 데이터프레임 대임
    columns_count+=len(df_dictionary[i].columns) # 컬럼 개수 추가
    if i != 0:
        df_dictionary[i]=pd.merge(df_dictionary[i-1],df_dictionary[i], on=['년도','월']) # 년도 와 월 을 기준으로 합침
        columns_count-=2 # 2개의 개수 기준으로 합침으로 2를 뺌


print('columns_count :',columns_count) # 개별 컬럼 개수들의 합
print('결과물 :',len(df_dictionary[len(file_lists)-1].columns)) # 통합하여 구한 컬럼의 개수, 제대로 통합이 되었는지 확인하기 위해서

# 중구, 북구, 남구등 겹치는 지역명이 _x, _y 등으로 명칭이 바뀜!
df_dictionary[len(file_lists)-1].to_csv('data_project_file/dataset/real_estate/부동산원_proprocessing2/통합.csv',  index = None,encoding='utf-8') # csv 파일로 저장