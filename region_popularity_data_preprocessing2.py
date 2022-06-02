# 이전에 저장한 인구 파일들을 지역별로 하나로 합쳐버리는 코드

from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
# pandas 라이브러리 import

import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용
import os

get_path_dir = 'C://self_project//data_project//data_project_file//dataset//region_popularity_ver1'
file_lists = os.listdir(get_path_dir)
df_dictionary = dict()
# print(len(file_lists)) # 파일이 5308개
file_name_list = list()

# for문을 통해서 여러 데이터 프레임들 생성
for i,file_list in enumerate(file_lists):
    print("make dataframe",i)
    df_dictionary[i] = pd.read_csv(get_path_dir+"//"+file_list, encoding='utf-8')
    df_dictionary[i].reset_index
    file_list = file_list.split("_")[:-1]
    file_list= "_".join(file_list) # file_list 이름이 00도_00시 꼴로 됨
    file_name_list.append(file_list)
    

for i in range(1,len(file_name_list)):
    print("make csv file",i)
    if file_name_list[i-1] == file_name_list[i]:
        df_dictionary[i]=pd.concat([df_dictionary[i-1], df_dictionary[i]], ignore_index=True)
    elif file_name_list[i-1] != file_name_list[i]:
        df_dictionary[i-1].set_index('카테고리')
        df_dictionary[i-1].to_csv('C://self_project//data_project//data_project_file//dataset//region_popularity_ver2//'+file_name_list[i-1]+'.csv', index=False) # 파일 저장
    
     



