# 셀레니움으로 저장한 인구데이터들 파일명 수정 및 컬럼명 수정 코드
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
# pandas 라이브러리 import

import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
import os

get_path_dir = 'C://self_project//covid_project//covid19_project//dataset//region_popularity_ver1'
file_lists = os.listdir(get_path_dir)
# for문을 통해서 여러 데이터 프레임들 생성
df = pd.read_csv(get_path_dir+"//"+"강원도_2020년03월.csv", encoding='utf-8')
print(df.index)
print(df)
print()
df.reset_index()
print(df)
     



