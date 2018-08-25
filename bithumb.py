import requests
import json
import datetime

url = "https://www.bithumb.com/resources/chart/BTC_xcoinTrade_24H.json?symbol=BTC"

response = requests.request("GET", url)

data = json.loads(response.text)

# 0, 1, 2, 3, 4, 5
# Timestamp, 시가, 종가, 고가, 저가, 거래량

for i in range(len(data)):
    print(str(datetime.datetime.fromtimestamp((data[i][0]/1000))) + "의 종가는 " + str(data[i][2]) + "원 입니다." + "\n") # 캔들 기준 시각(KST 기준)

print(datetime.datetime.now())

