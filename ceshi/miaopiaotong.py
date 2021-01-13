# -- coding:UTF-8 --<code>
# 查验发票测试1
import json
import requests
import hashlib
from Crypto.Cipher import AES
import base64

'''
采用AES对称加密算法
'''
# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
#加密方法
def encrypt_oracle():
    # 秘钥
    key = '123456'
    # 待加密文本
    text = 'abc123def456'
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))
    #用base64转成字符串形式
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    print(encrypted_text)
#解密方法
def decrypt_oralce(key,text):
    # 秘钥
    key = key
    # 密文
    text = text
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    #执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','') 
    print(decrypted_text)

def MD5(mima,shuihao):
    # md5加密
    m= hashlib.md5()  #创建md5对象
    #print('MD'+mima+shuihao)
    m.update(('MD'+mima+shuihao).encode("utf-8"))#生成加密串，其中password是要加密的字符串
    return(m.hexdigest())   #打印经过md5加密的字符串

def token(url,md001,md002,md003):
#token获取
    d = {'md001': md001, 'md002': md002, 'md003': md003}
    print(d)
    r=requests.post(url,data=json.dumps(d),headers={'Content-Type':'application/json'})
    print(r.json())
    s = json.dumps(r.json())
    s1 = json.loads(s)
    #print(s1['data'])
    return(s1['data'])

def chayan(url1,md004,md003,md010,invoices):
    d = {'md004': md004, 'md003': md003, 'md010': md010, 'invoices': invoices}
    print(d)
    r=requests.post(url1,data=json.dumps(d),headers={'Content-Type':'application/json'})
    print(r.json())
    s = json.dumps(r.json())
    s1 = json.loads(s)
    #print(s1)
    return(s1)

def aes():
    pass  

if __name__ == '__main__':
    usr='admin'
    mima='111'
    shuihao='91370100MA3ENBUB15'
    md002=MD5(mima,shuihao)
    #print(md002)
    url = 'http://120.27.52.219:8080/api-v1/auth/getToken'
    token=token(url,usr,md002,shuihao)
    print(token)

    url1='http://120.27.52.219:8080/api-v1/invoiceVerification/batchInspection'
    fpdm='1400193130'
    fphm='06178695'
    kprq='2020-04-16'
    value='95057.12'
    invoices="[{'fpdm':'"+fpdm+"','fphm':'"+fphm+"','kprq':'"+kprq+"','value':'"+value+"'}]"
    #print(invoices)
    jieguo=chayan(url1,token,shuihao,shuihao,invoices)
    jieguo1=jieguo['data'].replace('\r\n','')
    print(jieguo)
    key = 'czmd'+token[0:12]
    print(key)
    text = jieguo['data']
    print(text)
    
    #a = Prpcrypt(key).encrypt(text)
    b = decrypt_oralce(key,text)
    print(b)
    

