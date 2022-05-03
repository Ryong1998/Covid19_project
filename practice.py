import pandas as pd
from tabulate import tabulate # 데이터프레임을 예쁘게 출력하기 위해서 사용

df1 = pd.DataFrame({
    "x1": [100, 200, 300],
    "x2": [400, 500, 600],
    "x3": [700, 800, 900]},

     index=[2000, 2001, 2002]

)

df2 = pd.DataFrame({
    "x1": [1000, 2000, 3000],
    "x2": [4000, 5000, 6000],
    "x3": [7000, 8000, 9000]},

     index=[2010, 2011, 2012]

)

df3 = pd.DataFrame({
    "x1": [10000, 20000, 30000],
    "x2": [40000, 50000, 60000],
    "x3": [70000, 80000, 90000]},

     index=[2020, 2021, 2022]

)
df1.index.name = 'year'
df2.index.name = 'year'
df3.index.name = 'year'

for i in range(1,4):
    df0='df'+i
    print(tabulate(df0, headers='keys', tablefmt='psql'))
 

# print(tabulate(df1, headers='keys', tablefmt='psql'))
# print(tabulate(df2, headers='keys', tablefmt='psql'))
# print(tabulate(df3, headers='keys', tablefmt='psql'))
