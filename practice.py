import requests

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
params ={'serviceKey' : 'OtlfaJxmWNmyxJI3MPVTRTrJKBOe7Qks7%2FTcHRZscnpf2e%2B4oKSbfzCMhU4RewP3729MnEvUD0pJgzJ8DIh3VQ%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }

response = requests.get(url, params=params)
print(response.content)
