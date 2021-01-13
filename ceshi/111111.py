import datetime
def time():
    print (str(datetime.datetime.now()+datetime.timedelta(days=-61))[:11])
if __name__ =='__main__':
    time()