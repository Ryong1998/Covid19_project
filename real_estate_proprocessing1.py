# 부동산원 데이터를 형식에 맞춰서 전처리 하는 코드

from asyncio.windows_events import NULL
import pandas as pd

df = pd.read_csv('C://self_project//data_project//data_project_file//dataset//real_estate//부동산원_original/한국부동산원_전국주택가격동향조사_월간동향_아파트_매매가격(평균매매가격)_20210630.csv',encoding="cp949")
df=df.set_index('지 역') # 컬럼 '지 역'을 인덱스로 설정, 추후에 인덱스와 컬럼을 교환하기 위해서
df.index.name = NULL #'지 역'으로 되어있는 인덱스명을 null로 초기화 - 추후에 필요가 없어서
df=df.transpose() # 인덱스와 컬럼명들을 교체
df.index.name = '기간' # 바꾼 후, 인덱스명을 '기간'으로 설정 
df=df.reset_index('기간') # 인덱스를 다시 컬럼화, '기간'은 걸럼명이 됨
df['년도'] = df['기간'].str.split('-',expand=True)[0] # '년도'라는 컬럼명 추가
df['월'] = df['기간'].str.split('-',expand=True)[1] # '월'이라는 컬럼명 추가
df=df.astype({'년도':int}) # '년도'컬럼의 변수 타입 변경
df=df.astype({'월':int}) # '월' 컬럼의 변수 타입 변경

df=df[(df['년도']==2020) | (df['년도']==2021)]

del df['기간']
df=df.set_index(['년도','월'])

cols=df.columns.tolist()

col_dict={'서울':[],'경기':[],'인천':[],'부산':[],'대구':[],
              '광주':[],'대전':[],'울산':[],'강원':[],
              '충북':[],'충남':[],'전북':[],'전남':[],
              '경북':[],'경남':[],'제주':[],'기타':[]}

for col in cols:
    if ' 'in col:
        col_dosi=col.split(' ')[0]
        if col_dosi=='서울':
            col_dict['서울'].append(col)
        elif col_dosi=='경기':
            col_dict['경기'].append(col)
        elif col_dosi=='인천':
            col_dict['인천'].append(col)
        elif col_dosi=='부산':
            col_dict['부산'].append(col)
        elif col_dosi=='대구':
            col_dict['대구'].append(col)
        elif col_dosi=='광주':
            col_dict['광주'].append(col)
        elif col_dosi=='대전':
            col_dict['대전'].append(col)
        elif col_dosi=='울산':
            col_dict['울산'].append(col)
        elif col_dosi=='강원':
            col_dict['강원'].append(col)
        elif col_dosi=='충북':
            col_dict['충북'].append(col)
        elif col_dosi=='충남':
            col_dict['충남'].append(col)
        elif col_dosi=='전북':
            col_dict['전북'].append(col)
        elif col_dosi=='전남':
            col_dict['전남'].append(col)
        elif col_dosi=='경북':
            col_dict['경북'].append(col)
        elif col_dosi=='경남':
            col_dict['경남'].append(col)
        elif col_dosi=='제주':
            col_dict['제주'].append(col)
        else:
            col_dict['기타'].append(col)
    else:
        if col=='서울':
            col_dict['서울'].append(col)
        elif col=='경기':
            col_dict['경기'].append(col)
        elif col=='인천':
            col_dict['인천'].append(col)
        elif col=='부산':
            col_dict['부산'].append(col)
        elif col=='대구':
            col_dict['대구'].append(col)
        elif col=='광주':
            col_dict['광주'].append(col)
        elif col=='대전':
            col_dict['대전'].append(col)
        elif col=='울산':
            col_dict['울산'].append(col)
        elif col=='강원':
            col_dict['강원'].append(col)
        elif col=='충북':
            col_dict['충북'].append(col)
        elif col=='충남':
            col_dict['충남'].append(col)
        elif col=='전북':
            col_dict['전북'].append(col)
        elif col=='전남':
            col_dict['전남'].append(col)
        elif col=='경북':
            col_dict['경북'].append(col)
        elif col=='경남':
            col_dict['경남'].append(col)
        elif col=='제주':
            col_dict['제주'].append(col)
        else:
            col_dict['기타'].append(col)
            
for col_dict_key in col_dict.keys():
    # print(col_dict_key)
    df2=df[col_dict[col_dict_key]].copy()
    print(df2.head())
    df2.to_csv('data_project_file/dataset/real_estate/KB_proprocessing1/'+col_dict_key+'.csv', encoding='utf-8')
