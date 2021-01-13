# -- coding:UTF-8 --<code>
# 查验发票v1.0用于批量查询发票全票面，并入库明细
import json
from suds.client import Client
import pymysql
import xmltodict
import datetime
#以下是数据库连接以及写库操作
class DB():
    def __init__(self, host='', port=3306, db='', user='', passwd='', charset='utf8'):
        # 建立连接 
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型        
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)
    def __enter__(self):
        # 返回游标        
        return self.cur
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行        
        self.conn.commit()
        # 关闭游标        
        self.cur.close()
        # 关闭数据库连接        
        self.conn.close()
#以下是发票查验，返回查验结果模块
def chayan(invoicecode,invoiceno,times,checkcode):
    checkcode=checkcode[-6:] 
    chayan = Client('http://fpcy.sdaisino.com:8085/CheckCodeService/CXF/GetInvoiceService?wsdl')
    a=chayan.service.getInvoice('<?xml version="1.0" encoding="UTF-8"?><CheckData>\
    <InvData>\
    <TaxCode>91320982MA1MMPTCX9</TaxCode>\
    <Password>c4ca4238a0b923820dcc509a6f75849b</Password>\
    <InvCode>%s</InvCode>\
    <InvNo>%s</InvNo>\
    <InvTime>%s</InvTime>\
    <InvOther>%s</InvOther>\
    </InvData>\
    </CheckData>'%(invoicecode,invoiceno,times,checkcode))
    #print(a)
    a=a.replace('\'','')
    #print(a)
    my_dict = xmltodict.parse(a)
    return(my_dict)
#以下是成功发票结果入库操作模块
def gengxin(a,j,invoicecode,invoiceno,times,checkcode,id,Result,b,c):
    sql="update invoiceinfo set Gfmc=%s,Gfsh=%s,Gfdzdh=%s,Gfyhzh=%s,Xfmc=%s,Xfsh=%s,Xfdzdh=%s,Xfyhzh=%s,Je=%s,Se=%s,Jshj=%s,Bz=%s,Jqbm=%s,jym=%s,Fplx=%s,Result=%s,stype=%s where id = %s"
    arg=b
    with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
        db.executemany(sql,arg)#入库头信息
        print('查验入库成功%s'%j)
    sql2="INSERT INTO mingxi (invoiceid,invoicecode,invoiceno,row,Spmc,Ggxh,Jldw,Sl,Dj,Je,Slv,Se,Taxcode)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    arg=c
    with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
        db.executemany(sql2,arg)#入库明细信息
        print("明细入库成功")
#以下是发票票种识别，以及信息返回
# 01：专用发票:
# 增值税专用发票：10位，第1～4位代表各省；第5～6位代表制版年度；第7位代表印制批次；第8位代表发票种类，普通发票用“6”表示；第9位代表几联版，二联版用“2”表示，五联版用“5”表示；第10位代表金额版本号，“0”表示电脑版。
# 二手车专用发票：12位，第1位为0；第2-5位代表省、自治区、直辖市和计划单列市；第6-7位代表年度；第8-10位代表批次；第11-12位为17
# 机动车销售发票：12位，发票代码前五位为 税务机关代码 11100  第八位数字为2
# 04：普票发票:12位，第1位为0;第2-5位代表省、自治区、直辖市和计划单列市;第6-7位代表年度;第8-10位代表批次;第11-12位代表票种和联次，其中04代表二联增值税普通发票、05代表五联增值税普通发票。
# 10：电子发票:12位，
# 电子普通发票：第1位为0；第2-5位代表省、自治区、直辖市和计划单列市；第6-7位代表年度；第8-10位代表批次；第11-12位代表票种(11代表增值税电子普通发票)。
# 电子通行费：第1位为0；第2-5位代表省、自治区、直辖市和计划单列市；第6-7位代表年度；第8-10位代表批次；第11-12位为12；
# 11：卷式发票:12位，第1位为0；第2-5位代表省、自治区、直辖市和计划单列市；第6-7位代表年度,第8-10位代表批次；第11-12位代表票种和规格；其中06代表57mm×177.8mm增值税普通发票(卷票)；07代表76mm×177.8mm增值税普通发票(卷票).
def piaozhong(invoicecode):
    if len(invoicecode) == 12:
        if invoicecode[:1] == '0':
            if invoicecode[-2:] == '04':#增值税普通2联发票
                return({'code':'04','name':'增值税普通2联发票'})
            elif invoicecode[-2:] == '05':#增值税普通5联发票
                return({'code':'04','name':'增值税普通5联发票'})
            elif invoicecode[-2:] == '06':#增值税卷式57mm窄票
                return({'code':'04','name':'增值税卷式57mm窄票'})
            elif invoicecode[-2:] == '07':#增值税卷式76mm宽票
                return({'code':'04','name':'增值税卷式76mm宽票'})
            elif invoicecode[-2:] == '11':#增值税电子普通发票
                return({'code':'10','name':'增值税电子普通发票'})
            elif invoicecode[-2:] == '12':#增值税电子通行费发票
                return({'code':'10','name':'增值税电子通行费发票'})
            elif invoicecode[-2:] == '17':#增值税二手车交易发票
                return({'code':'01','name':'增值税二手车交易发票'})
        else:
            return({'code':'01','name':'机动车统一销售发票'})#机动车统一销售发票
    elif len(invoicecode) == 10:
        return({'code':'01','name':'增值税专用发票'})#增值税专用发票
    else:
        return({'code':'99','name':'无法查验票种'})#无法查验票种
#去除None值
def k(none):
    if none is None:
        return ''#将Python空类型转换为数据库可识别空值
    else:
        return none#否则正常返回
if __name__ == '__main__':
    xunhuan=500#分割循环变量
    with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
        db.execute("select count(*) from invoiceinfo where Result = ''")#计算待查询数据量，默认Result有值不查询
    for i in db:#计算需整循环次数，以及剩余次数
        x=int(i['count(*)'])//xunhuan
        y=int(i['count(*)'])%xunhuan
        print(x,y)
    j=1#整循环发票张数计次
    l=0#零循环张数计次
    a={}#用于接收票种返回字典code，name
    b=[]#批量待更新头信息保存list
    c=[]#批量待更新明细信息list  
    if x > 0:#整循环判断
        for i in range(1,x+1):
            # print(i)
            with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
                db.execute("select * from invoiceinfo where Result = '' LIMIT %s"%xunhuan)    
            for s in db:
                print("组装第%s张发票数据发票id：%s"%(j,s['id']))
                a=piaozhong(s['invoicecode'])#进行票种查询
                if a['code'] == '04' or a['code'] == '10'or a['code'] == '11':#票种判断，用以选择提交查验信息
                    s['checkcode']=s['checkcode']
                elif a['code'] == '01':
                    s['checkcode']=s['total']
                else:
                    print("查验第%s张发票,发票ID：%s，无法查验票种"%(j,s['id']))#无法查验票种结果直接入库
                    sql="update invoiceinfo set Result ='%s',stype='%s' where id = %s"%("无法查验票种",a['name'],s['id'])
                    with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
                        db.execute(sql)
                    j=j+1
                    continue
                my_dict=chayan(s['invoicecode'],s['invoiceno'],s['times'],s['checkcode'])#提交查验获取查验后格式报文，返回字典
                if my_dict['Data']['Result']['Code'] != '1':#查验不成功信息处理    
                    sql="update invoiceinfo set Result ='%s',stype='%s' where id = %s"%(my_dict['Data']['Result']['Message'],a['name'],s['id'])
                    with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:#不成功信息直接入库
                        db.execute(sql.replace('None',''))
                    print("查验第%s张发票,发票ID：%s,发票票种：%s,%s"%(j,s['id'],my_dict['Data']['Result']['Message'],a['name']))
                    j=j+1
                else:#查验成功，报文拆解
                    Fp=my_dict['Data']['Fp']
                    # Gfmc,Gfsh,Gfdzdh,Gfyhzh,Xfmc,Xfsh,Xfdzdh,Xfyhzh,Je,Se,Jshj,Bz,Jqbm,jym,Fplx,Result,stype,id
                    b.append((k(Fp['Gfmc']),k(Fp['Gfsh']),k(Fp['Gfdzdh']),k(Fp['Gfyhzh']),k(Fp['Xfmc']),k(Fp['Xfsh']),k(Fp['Xfdzdh']),\
                        k(Fp['Xfyhzh']),k(Fp['Je']),k(Fp['Se']),k(Fp['Jshj']),k(Fp['Bz']),k(Fp['Jqbm']),k(Fp['JYM']),k(Fp['Fplx']),\
                            k(my_dict['Data']['Result']['Message']),k(a['name']),k(s['id'])))#头信息组装
                    Sph=Fp['Sph']
                    if isinstance(Sph,dict):#明细信息组装，如果单行商品则为字典，多行商品为字典列表
                        c.append((s['id'],s['invoicecode'],s['invoiceno'],Fp['Sph']['Xh'],k(Fp['Sph']['Spmc']),k(Fp['Sph']['Ggxh']),\
                            k(Fp['Sph']['Ggxh']),k(Fp['Sph']['Sl']),k(Fp['Sph']['Dj']),k(Fp['Sph']['Je']),k(Fp['Sph']['Slv']),k(Fp['Sph']['Se']),k(Fp['Sph']['Taxcode'])))
                    else:
                        for i in Fp['Sph']:#多行商品循环组装
                            c.append((s['id'],s['invoicecode'],s['invoiceno'],i['Xh'],k(i['Spmc']),k(i['Ggxh']),k(i['Jldw']),k(i['Sl']),\
                                k(i['Dj']),k(i['Je']),k(i['Slv']),k(i['Se']),k(i['Taxcode'])))
                    j=j+1
            gengxin(a,j,s['invoicecode'],s['invoiceno'],s['times'],s['checkcode'],s['id'],my_dict['Data']['Result']['Message'],b,c)#整循环提交组装结果，调用数据库入库      
    elif y > 0:#零循环
        with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
            db.execute("select * from invoiceinfo where Result = ''limit %s"%y)       
        for s in db:
            print("组装第%s张发票数据"%(j+l))
            #print(i)
            a=piaozhong(s['invoicecode'])
            if a['code'] == '04' or a['code'] == '10'or a['code'] == '11':
                s['checkcode']=s['checkcode']
            elif a['code'] == '01':
                s['checkcode']=s['total']
            else:
                print("查验第%s张发票,发票ID：%s，无法查验票种"%((j+l),s['id']))
                sql="update invoiceinfo set Result ='%s',stype='%s' where id = %s"%("无法查验票种",a['name'],s['id'])
                with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
                    db.execute(sql)
                l=l+1#零循环张数计数
                continue
            my_dict=chayan(s['invoicecode'],s['invoiceno'],s['times'],s['checkcode'])
            #print(s['times'],my_dict)
            if my_dict['Data']['Result']['Code'] != '1':
                sql="update invoiceinfo set Result ='%s',stype='%s' where id = %s"%(my_dict['Data']['Result']['Message'],a['name'],s['id'])
                with DB(host='localhost',user='root',passwd='aisino2017',db='yidong') as db:
                    db.execute(sql.replace('None',''))
                print("查验第%s张发票,发票ID：%s,发票票种：%s,%s"%((j+l),s['id'],my_dict['Data']['Result']['Message'],a['name']))
                l=l+1
            else:
                Fp=my_dict['Data']['Fp']
                    # Gfmc,Gfsh,Gfdzdh,Gfyhzh,Xfmc,Xfsh,Xfdzdh,Xfyhzh,Je,Se,Jshj,Bz,Jqbm,jym,Fplx,Result,stype,id
                b.append((k(Fp['Gfmc']),k(Fp['Gfsh']),k(Fp['Gfdzdh']),k(Fp['Gfyhzh']),k(Fp['Xfmc']),k(Fp['Xfsh']),k(Fp['Xfdzdh']),\
                    k(Fp['Xfyhzh']),k(Fp['Je']),k(Fp['Se']),k(Fp['Jshj']),k(Fp['Bz']),k(Fp['Jqbm']),k(Fp['JYM']),k(Fp['Fplx']),\
                        k(my_dict['Data']['Result']['Message']),k(a['name']),k(s['id'])))
                Sph=Fp['Sph']
                if isinstance(Sph,dict):
                    c.append((s['id'],s['invoicecode'],s['invoiceno'],Fp['Sph']['Xh'],k(Fp['Sph']['Spmc']),k(Fp['Sph']['Ggxh']),\
                        k(Fp['Sph']['Ggxh']),k(Fp['Sph']['Sl']),k(Fp['Sph']['Dj']),k(Fp['Sph']['Je']),k(Fp['Sph']['Slv']),k(Fp['Sph']['Se']),k(Fp['Sph']['Taxcode'])))
                else:
                    for i in Fp['Sph']:
                        c.append((s['id'],s['invoicecode'],s['invoiceno'],i['Xh'],k(i['Spmc']),k(i['Ggxh']),k(i['Jldw']),k(i['Sl']),\
                            k(i['Dj']),k(i['Je']),k(i['Slv']),k(i['Se']),k(i['Taxcode'])))
                l=l+1
        gengxin(a,(j+l),s['invoicecode'],s['invoiceno'],s['times'],s['checkcode'],s['id'],my_dict['Data']['Result']['Message'],b,c)#零循环提交组装结果，调用数据库入库 
    else:
        pass