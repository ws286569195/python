import urllib.request
import json
   # print(load_f)
with open('city.json', 'r', encoding='UTF-8') as load_f:
    load_f = json.load(load_f)
i = input('输入城市名称：')
a = 0
b = 0
for n in load_f:
    a = a + 1
    cityName = n['cityName']
    province = n['province']
    cityPinyin = n['cityPinyin']
    cityCode = n['cityCode']
    # print(cityName,province,cityPinyin,cityCode)
    # print(i)
    if i == cityName:
        print(cityName,province,cityPinyin,cityCode)
        b =cityCode
        break
    elif i == province:
        print(cityName,province,cityPinyin,cityCode)
        b =cityCode
        break
    elif i == cityPinyin:
        print(cityName,province,cityPinyin,cityCode)
        b =cityCode
        break
    else:
        if a == len(load_f):
            print('未检索到城市名字！')
            break
url = 'http://t.weather.sojson.com/api/weather/city/'
url = url + str(b)
print(url)
r = urllib.request.urlopen(url)
htlm = r.read()
print(htlm.decode('utf-8'))