# 이전에 저장한 파일들을 지역과 성별을 기준으로 합치고, 시간 나이대별로 분류를 함
# 파일명 : 지역_성별_나이대       /   인덱스 : 시간 컬럼으로 년 월 구분해서 생성하기  컬럼: 상세지역들

from numpy import int64
import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
import os

# 행들을 인자로 받아서 '나이'컬럼에 해당하는 컬럼값들을 수정
def func(df_data):
    if '~' in df_data['나이']:
        df_data['나이']=df_data['나이'].split('~')[0]
    elif df_data['나이'] == '100세 이상':
        df_data['나이']='100'   
    elif df_data['나이'] == '총인구수':
        df_data['나이']=df_data['나이'][0]
    return df_data

df_dict = dict() 

path_dir = "C://self_project//covid_project//covid19_project//dataset//region_popularity_ver2"
file_lists = os.listdir(path_dir) # file_lists의 요소들은 .csv까지 문자열로 포함되어 있다

for file_list in file_lists: 
   
    file_name = file_list.split('.')[0] # 파일 저장을 할 때 file_list는 .csv까지 붙여져 있어서 더 깔끔하게 이름을 설정하기 위해서 전처리
    
    # 임시 테스트를 위해서 파이 하나 만을 읽음
    df = pd.read_csv(path_dir+'//'+file_list,  encoding='utf-8') # 추후 수정 필요

    # 년도와 월을 컬럼으로 추가
    df['년월'] = df['카테고리'].str.split('_',expand=True)[0]
    df['년도'] = df['년월'].str.split('년',expand=True)[0]
    df['월'] = df['년월'].str.split('년',expand=True)[1].str.split('월',expand=True)[0]

    # 성별을 컬럼을 추가
    df['성별'] = df['카테고리'].str.split('_',expand=True)[1]

    # 나이를 컬럼으로 추가
    df['나이'] = df['카테고리'].str.split('_',expand=True)[2]

    # 년도 와 월 컬럼을 정수형으로 변환
    df=df.astype({'년도':int64})
    df=df.astype({'월':int64})


    # '나이' 컬럼 전처리, apply 를 통해 func 함수를 적용
    df = df.apply(func, axis=1)

    # '나이' 컬럼에서 값이 '총인구수'인 값들을 샂제
    df = df.set_index('나이')
    df = df.drop('연령구간인구수')
    df = df.reset_index('나이')

    # 년 월 나이를 인덱스로 하기
    df = df.set_index(['년도','월','나이'])

    # 카테고리 년월 컬럼명 삭제
    del df['카테고리']
    del df['년월']

    # 카테고리별로 데이터프레임을 생성
    df_dict['whole'] = df[df['성별']=='계'].copy()
    df_dict['male'] = df[df['성별']=='남'].copy()
    df_dict['female'] = df[df['성별']=='여'].copy()

    for df_dict_key in df_dict.keys():
        del df_dict[df_dict_key]['성별'] # 데이터프레임들에 있는 성별 컬럼은 이제 필요 없음
        df_dict[df_dict_key].to_csv('covid19_project/dataset/region_popularity_ver3/'+file_name+'_'+df_dict_key+'.csv', encoding='utf-8')
    
    # 진행상황을 알기위해서 진행중인 원본 파일 출력
    print(file_list+" 완료")