import pandas as pd
from asyncio.windows_events import NULL

df = pd.read_csv('C://self_project//data_project//data_project_file//dataset//real_estate//KB_original2/월간 아파트 매매가격지수.csv',encoding='utf-8')
df = df.set_index('지역명') # 지역명 컬럼을 인덱스로 설정
df.index.name = NULL # 인덱스명을 빈 값으로 설정
df=df.transpose() # 인덱스와 컬럼들을 교체
df=df.reset_index() # 인덱스를 다시 컬럼화 시킴
df['년도']= df['index'].str.split('-',expand=True)[0] # '년도' 컬럼 생성
df['월']= df['index'].str.split('-',expand=True)[1] # '월' 컬럼 생성


df=df.astype({'년도':int}) # 년도 컬럼의 타입 변경
df=df.astype({'월':int}) # 월 컬럼의 타입 변경
df=df[(df['년도']==2020) | (df['년도']==2021)] # 년도 컬럼에서 해당하는 부분들만 사용
del df['index'] # 'index'라는 컬럼 삭제

df = df.set_index(['년도','월']) # '년도' 컬럼과 '월'컬럼을 인덱스로 설정
df.to_csv('data_project_file/dataset/real_estate/KB_preprocessing1/KB아파트매매지수.csv', encoding='utf-8') # csv 파일로 저장