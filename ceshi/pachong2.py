import requests
import re
headers = {'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'X-Requested-With':'XMLHttpRequest'
}
data = {
    'type':'CLIENT-HELLO',
    'clientHello':'3077020103305E310B300906035504061302636E31153013060355040B1E0C56FD5BB67A0E52A1603B5C40311D301B06035504031E147A0E52A175355B508BC14E667BA174064E2D5FC331193017060355040D1E100063006100310030003000300030003202071E010000322A55A209310702010102020402',
    'alg':'0',
    'ymbb':'4.0.04'
}
url ='https://fpdk.qingdao.chinatax.gov.cn//NSbsqWW/login.do'
r = requests.post(url,headers = headers,data = data,verify=False)
r=r.text
print(r)
print("key1",re.findall(".*key1\":\"(.*)\",\"key2.*",r))
print("key2",re.findall(".*key2\":\"(.*)\",\"key3.*",r))
print("key3",re.findall(".*key3\":\"(.*)\".*",r))
url = 'https://fpdk.shandong.chinatax.gov.cn/NSbsqWW/querymm.do'
data = {
    'cert':'913701007262083531',
    'funType':'01'
}
r = requests.post(url,headers = headers,data = data,verify=False)
r=r.text
print(r)
# session = requests.Session()
# session.post(url,headers = headers,data = data,verify=False)
# print(session.post(url,headers = headers,data = data))
# response = session.get('https://www.itjuzi.com/investevent/11065968',headers = headers,verify=False)
# print(response)
# print(response.status_code)
# print(response.text)
