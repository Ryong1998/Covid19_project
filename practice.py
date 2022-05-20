columns_list= ["경기도 군포시 (4141000000)", "경기도 군포시 군포1동(4141051000)","서울특별시  (1100000000)"]
for i,column_value in enumerate(columns_list):
    columns_list[i] = column_value.split('(')[0]
    if columns_list[i][-1]==' ':
        columns_list[i]=columns_list[i].split()
        columns_list[i] = " ".join(columns_list[i])

print(columns_list)