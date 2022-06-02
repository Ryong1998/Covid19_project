import pandas as pd
from asyncio.windows_events import NULL

df = pd.read_csv('C://self_project//data_project//data_project_file//dataset//real_estate//KB_original2/월간 아파트 매매가격지수.csv',encoding='utf-8')
df = df.set_index('지역명')
df.index.name = NULL
df=df.transpose()
df=df.reset_index()
df['년도']= df['index'].str.split('-',expand=True)[0]
df['월']= df['index'].str.split('-',expand=True)[1]


df=df.astype({'년도':int})
df=df.astype({'월':int})
df=df[(df['년도']==2020) | (df['년도']==2021)]
del df['index']

df = df.set_index(['년도','월'])
df.to_csv('data_project_file/dataset/real_estate/KB_preprocessing1/KB아파트매매지수.csv', encoding='utf-8')