from datetime import datetime as dt
from datetime import timedelta
import pandas as pd


def getExcel(startday):
    # 开始时间变成datetime对象，一个月产生2个xlsx
    dt_startDay = dt.strptime(startday,"%Y%m")
    # dt_endDay = dt.strptime(startday,"%Y/%m")

    dt_startDay1 = dt_startDay.replace(day=1).strftime('%Y%m%d')
    dt_endDay1   = dt_startDay.replace(day=15).strftime('%Y%m%d')
    dt_startDay2 = dt_startDay.replace(day=16).strftime('%Y%m%d')
    if dt_startDay.month == 12:
        dt_endDay2 = (dt_startDay.replace(day=1, month=1, year=dt_startDay.year+1) - timedelta(days=1)).strftime('%Y%m%d')
        returnDay = dt_startDay.replace(day=1, month=1, year=dt_startDay.year+1).strftime('%Y%m')
    else:
        dt_endDay2   = (dt_startDay.replace(day=1,month=dt_startDay.month+1)-timedelta(days=1)).strftime('%Y%m%d')
        returnDay = dt_startDay.replace(day=1,month=dt_startDay.month+1).strftime('%Y%m')
    print(dt_startDay1)
    print(dt_endDay1)
    print(dt_startDay2)
    print(dt_endDay2)

    df.to_excel(path + dt_startDay1 + '_' + dt_endDay1 + '.xlsx')
    df.to_excel(path + dt_startDay2 + '_' + dt_endDay2 + '.xlsx')
    print(returnDay)
    return returnDay





df = pd.DataFrame()

path = r'D:\快消七剑\Data\A_订单\ECRC\test\\'
# getExcel('2018/12')
startday = '201807'
endday = '201906'
# interval = 14
while True:
    if startday>endday:
        break
    startday = getExcel(startday)
