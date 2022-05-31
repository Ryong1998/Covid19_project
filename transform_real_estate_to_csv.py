# 부동산 관련 엑셀 파일들을 csv 파일들로 변환

import pandas as pd
import os

get_path_dir = 'C://self_project//covid_project//covid19_project//dataset//real_estate//original' # 원본인 엑셀 파일들이 담린 경로를 저장
file_lists = os.listdir(get_path_dir) # 경로에 저장된 파일들을 file_lists에 저장
for file_list in file_lists:
    read_file = pd.read_excel ('C://self_project//covid_project//covid19_project//dataset//real_estate//original//'+file_list) # 엑셀 파일을 읽어서 read_file 변수에 저장
    file_list = file_list.split(".")[0] # 파일명을 보다 깔끔하게 하기 위해서 split 부분 이용
    read_file.to_csv ('C://self_project//covid_project//covid19_project//dataset//real_estate//original2//'+file_list+".csv", index = None, header=True) # 원본 파일을 csv 파일로 저장