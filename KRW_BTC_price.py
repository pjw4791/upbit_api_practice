import requests
import multiprocessing
import random
import datetime
import talib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

url = "https://api.upbit.com/v1/candles/days"

querystring = {"market":"KRW-BTC", "count":100}

response = requests.request("GET", url, params=querystring)

print(response.text)

dataset = {}
count = 0
# timeframe 을 바꾸고 싶으면 아래 파일명을 86400 대신 21600, 3600 으로 바꾸시면 됩니다.
with open('./crypto.bithum.86400.csv', 'r') as fp:
    for row in fp:
        ts, currency, O, H, L, C, V = row.strip().split(',')
        ts = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
        if currency not in dataset:
            dataset[currency] = dict(ts=[], O=[], H=[], L=[], C=[], V=[])

        dataset[currency]['ts'].append(ts)
        dataset[currency]['O'].append(float(O))
        dataset[currency]['H'].append(float(H))
        dataset[currency]['L'].append(float(L))
        dataset[currency]['C'].append(float(C))
        dataset[currency]['V'].append(float(V))
        count += 1

print('Total number of rows: {}'.format(count))