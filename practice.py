import requests
import json
import datetime

url = "https://api.upbit.com/v1/candles/days"

querystring = {"market":"KRW-BTC", "count":1000}

response = requests.request("GET", url, params=querystring)

data = json.loads(response.text)
# print(type(response.text))
# print(response.text)
# print(type(data))
# print(len(data))

for i in range(len(data)):
    if i==0:
        print('{:.10}'.format(data[i]['candle_date_time_kst']) + "의 현재 거래가는 " + str(data[i]['trade_price']) + "원 입니다." + "\n") # 캔들 기준 시각(KST 기준)
    else:
        print('{:.10}'.format(data[i]['candle_date_time_kst']) + "의 종가는 " + str(data[i]['trade_price']) + "원 입니다." + "\n") # 캔들 기준 시각(KST 기준)
# print(data[0]['prev_closing_price']) # UTC 0시 기준

# print(datetime.datetime.now())