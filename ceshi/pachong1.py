
from bs4 import BeautifulSoup
import requests,re
if __name__ == '__main__':
    n=1
    j=1
    while n<=681:
        url = 'https://www.quanji789.com/vod-search-wd--p-%s.html' %n
        req = requests.get(url=url,timeout = 5000)
        html=req.text
        bf = BeautifulSoup(html)
        for link in bf.find_all('ol'):
            xuhao=link.find('em').string
            a=link.find('a').string
            b="https://www.quanji789.com"+ link.find('a')['href']
            leixing=link.find('b').string
            time=link.find('strong').string
            print ("序号：%s——名字：%s——地址：%s——类型：%s——更新时间：%s" %(xuhao,a,b,leixing,time))
            f = open('E:/test.txt','a',encoding='utf-8')
            f.writelines(['\n',"序号：",str(j),"影片名称：",a,"影片地址：",b,"影片类型：",leixing,"更新时间：",time])
            f.close()
            j=j+1
        n=n+1


