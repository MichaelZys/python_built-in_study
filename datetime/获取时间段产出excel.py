from datetime import datetime as dt
from datetime import timedelta
import pandas as pd


def getExcel(startday, interval):
    # 开始时间变成datetime对象，向后加n天
    dt_startDay = dt.strptime(startday,"%Y/%m/%d")
    if dt_startDay.day == 26:
        dt_endDay = dt_startDay.replace(month=dt_startDay.month+1,day=1)-timedelta(days=1)
    else:
        dt_endDay = dt_startDay + timedelta(days=interval)
    dt_startDay_month = dt_startDay.month
    dt_endDay_month = dt_endDay.month
    if dt_startDay_month != dt_endDay_month:
        dt_endDay = dt_startDay + timedelta(days=10)
        dt_endDay = dt_endDay.replace(day=1)-timedelta(days=1)
    # a = lambda dt_endDay.month:'0'+str(dt_endDay.month) if len(dt_endDay.month)==1
    print(dt_startDay.__format__('%Y%m%d'))


    endDay = '0'+str(dt_endDay.day) if len(str(dt_endDay.day))==1 else str(dt_endDay.day)
    endMon = '0'+str(dt_endDay.month) if len(str(dt_endDay.month))==1 else str(dt_endDay.month)
    # print(strMon+strDay)
    print(endMon+endDay)
    # print(type(dt_endDay.month))
    df.to_excel(path+dt_startDay.__format__('%Y%m%d')+'_'+endMon+endDay+'.xlsx')
    print(dt_startDay)
    print(dt_endDay)
    return (dt_endDay+timedelta(days=1)).__format__('%Y/%m/%d')




df = pd.DataFrame()

path = r'D:\快消七剑\Data\A_订单\ECRC\test\\'
startday = '2018/07/01'
interval = 4
while True:
    startday = getExcel(startday,interval)
