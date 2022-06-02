# 코로나 데이터셋을 그래프로 시각화하는 코드

import pandas as pd
#plotly를 이용하기 위해서 import
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('data_project_file///dataset/covid_base/covid_base_data_1.csv',encoding="utf-8")

# 그래프로 출력할 두개의 column 명을 변수로 받음
first_measurement='일일확진자수'
second_measurement='일일검사자수'

#fig = go.Figure() #그래프를 그리고 위해 함수 불러옴

fig = make_subplots(specs=[[{"secondary_y": True}]]) # 두개의 다른 y축 그래프를 생성하기 위해서 생성

# 첫번째 x축 y축에 대한 정보 생성
fig.add_trace(
    go.Scatter(    
        x=df.index, y=df[first_measurement], mode='lines', name=first_measurement
    ),secondary_y=False
)

# 두번째 x축 y축에 대한 정보 생성
fig.add_trace(
    go.Scatter(
        x=df.index, y=df[second_measurement], mode='lines', name=second_measurement
    ),
    secondary_y=True #두개의 y축 사용을 위해서
)

# 그래프에서 제목 및 x축 layout들 입력
fig.update_layout(
    {
        "title": {
            "text": "Daily Covid19 Decide",
            "font": {
                "size": 15
            }
        },
        "showlegend": True, #옆에 trace0 표시
        "xaxis": {
            "title": "Date"
        }
    }
)

# 그래프 y축 layout들 입력
fig.update_yaxes(title_text='<b>'+first_measurement+'</b>', secondary_y=False)
fig.update_yaxes(title_text='<b>'+second_measurement+'</b>', secondary_y=True)

fig.show() # 생성한 그래프를 출력