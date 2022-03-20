import pandas as pd
from tabulate import tabulate

df = pd.DataFrame({
    "컬럼명1": [1, 2, 3],
    "컬럼명2": [4, 5, 6],
    "컬럼명3": [7, 8, 9]},

     index=[2019, 2020, 2021]

)
df.index.name = '연도'
print(df)
print(tabulate(df, headers='keys', tablefmt='psql'))