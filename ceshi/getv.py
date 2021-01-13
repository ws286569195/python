# -- coding:UTF-8 --<code>
import pymysql
import urllib.request
import time
import qrcode
import image
import datetime
import random
listb = []
#信息查询 
def chaxun(count):
    # 数据库连接
    db = pymysql.connect('172.18.14.65','root','aisino2017','xxfpglxt')
    # 初始化游标
    cursor = db.cursor()
    # 数据库查询
    sql ="SELECT applyflag,number,taxmoney,status,id FROM billinfo WHERE infokind = '51' AND total >= '50' AND status = '1' AND times = '%s' AND sellertaxcode = '91370100267180207R' LIMIT %s"%(str(datetime.datetime.now()+datetime.timedelta(days=-61))[:11],count)
    print(sql)
    lista = cursor.execute(sql)
    all_data = cursor.fetchall()
    #print(all_data)
    return(all_data)
    # 关闭数据库连接
    db.close()
#信息生产
def tijiao():
    for data in chaxun(count):
        time.sleep(random.randint(500,1000))
        # url拼接请求
        #url1 = 'http://172.18.14.51:8086/FPGLXT_WX/bill/applyKp.action?number='+data[1]+'&clientname=%E4%B8%AA%E4%BA%BA&clienttax=&clientaddress=&clientbank=&clientmail=&taxmoney='+str(data[2])
        url1 = 'http://fapiao.uni-mart.com.cn:8086/FPGLXT_WX/bill/applyKp.action?number='\
            +data[1]+'&clientname=%E4%B8%AA%E4%BA%BA&clienttax=&clientaddress=&clientbank=&clientmail=&taxmoney='+str(data[2])
        listb.append(data[1])
        print(url1)
        response1 = urllib.request.urlopen(url1)
        #print(response1)
#图片生产
def shengcheng(listb):
    # 数据库连接
    db = pymysql.connect('172.18.14.65','root','aisino2017','xxfpglxt')
    # 初始化游标
    cursor = db.cursor()
    # 数据库查询
    for info in listb:
        print(info)
        inv = cursor.execute("SELECT invoicecode,invoiceno,total,times FROM invoiceinfo WHERE number ="+"'"+str(info)+"'")
        inv = cursor.fetchone()
        #print(inv)
        qrcode.make(',10,'+str(inv[0])+','+str(inv[1])+','+str(str(inv[2]))+','+str(inv[3])[:4]+str(inv[3])[5:7]+str(inv[3])[8:10]+',,A,').get_image().save('png/'+str(inv[3])+'-'+str(inv[1])+'.png')
    # 关闭数据库连接
    db.close()
#生产结果随机头信息
def xiushi(listb,count):
    # 数据库连接
    db = pymysql.connect('172.18.14.65','root','aisino2017','xxfpglxt',charset='utf8')
    # 初始化游标
    cursor = db.cursor()
    # 数据库查询
    for info in listb:
        print(info)
        sql ="SELECT clientname FROM clientinfo order by rand() LIMIT %s"%count
        #print(sql)
        inv =cursor.execute(sql)
        inv = cursor.fetchone()
        print(inv[0])
        sql = "UPDATE invoiceinfo set clientname = '%s' WHERE number = '%s'"%(inv[0],info)
        #print(sql)
        cursor.execute(sql)
        db.commit()
    # 关闭数据库连接
    db.close()
if __name__ == '__main__':
    # inv信息查询
    # listb=[11700200021620200202,17805200031020200202,16300200041020200202,17900100028420200202,10401200061020200202]
    #生成数量
    count = 10
    tijiao()
    time.sleep(100)
    print(listb)
    shengcheng(listb)
    xiushi(listb,count)

