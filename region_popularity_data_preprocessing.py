# 셀레니움으로 저장한 인구데이터들 파일명 수정 및 컬럼명 수정 코드

# pandas 라이브러리 import

import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
import os

path_dir = 'C://self_project//covid_project//covid19_project//dataset//region_popularity'
file_lists = os.listdir(path_dir)
for file_list in file_lists:

    # csv 파일 읽기, 경로는 상대경로, 절대경로 중 선택해서 기입
    df = pd.read_csv("C://self_project//covid_project//covid19_project//dataset//region_popularity//"+file_list, encoding='cp949')
    df = df.set_index('행정구역') # 데이터프레임의 인덱스 설정


    df = df.transpose() # 데이터 프레임의 컬럼들과 인덱스 설정(기존에는 인덱스가 지역, 컬럼이 연령별 카테고리 였는데 인덱스를 연령별 카테고리로, 컬럼을 지역으로 설정)
    season=df.index[0].split("_")[0] # 0000년00월 을 변수에 담음
    region_dosi = df.columns[0].split()[0] #행정구역 중 도 or 시를 변수에 담는다 

    region_sigungu = '_'+df.columns[0].split()[1]+"_" # 행정구역 중 시군구를 변수에 담는다. 앞 뒤 "_"는 후에 파일명을 만들 때 도움이 되기 위해서 붙임
    if '(' in region_sigungu: # 시군구가 따로 없이 도 시만 있는 경우는 시군구 부분을 "_"로 처리, 후에 파일명을 만들 때 도움이 되기 위해서
        region_sigungu = "_"

    columns_list = list(df.columns) # 컬럼명들을 리스트화 한 리스트를 생성, 코드로 있는 (0000000000) 부분을 지우기 위해서
    # print(columns_list)

    for i,column_value in enumerate(columns_list): # 위에서 생성한 리스트의 요소들에 대해서 실행
        columns_list[i] = column_value.split('(')[0] # '('을 기준으로 자르고 앞에 부분을 우선 남김
        if columns_list[i][-1]==' ': # 남은 부분의 마지막 글자가 ' ' 일때, 예를 들어 '서울특별시 ' 일때
            columns_list[i]=columns_list[i].split() # 공백 기준으로 나누고 내용이 있는 부분들만 값으로 남김
            columns_list[i] = " ".join(columns_list[i]) # 남은 요소들을 ' ' 을 중간으로 넣어서 합침
        
        
    df.columns=columns_list # 데이터 프레임의 컬럼명들을 정규식처리한 컬럼명들로 변경



    # print(columns_list)

    # # 만든 데이터 프레임 출력
    # print(tabulate(df, headers='keys', tablefmt='psql'))

    # print("index!!!!")
    # print(df.index) # 데이터 프레임의 인덱스 확인
    # print("columns!!!!")
    # print(df.columns) # 데이터 프레임의 컬럼들 확인
    # print()
    # print()

    filename = region_dosi+region_sigungu+season
    print(filename) # 만들고자 하는 파일명 임시적 확인

    df.to_csv('C://self_project//covid_project//covid19_project//dataset//region_popularity_ver1//'+filename+'.csv') # 파일 저장