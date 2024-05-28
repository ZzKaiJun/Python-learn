
import time
import datetime
import pytz


def utc_to_local(utc_time_str, local_format="%Y-%m-%d %H:%M:%S", utc_format=f'%Y-%m-%dT%H:%M:%S'):
    local_tz = pytz.timezone('Asia/Chongqing')
    print(local_tz)  # Asia/Chongqing 改变时区
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    print(utc_dt)  # 2019-08-06 15:59:39 把 str 转成 时间格式
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    print(local_dt)  # 2019-08-06 23:59:39+08:00  utcs时间 转换时区
    time_str = local_dt.strftime(local_format)
    print(time_str)  # time.struct_time(tm_year=2019, tm_mon=8, tm_mday=6, tm_hour=23, tm_min=59, tm_sec=39, tm_wday=1, tm_yday=218, tm_isdst=0) 把时间转成字符串
    ltime = time.strptime(time_str, local_format)  # 2019-08-06 23:59:39
    print(type(time.strptime(time_str, local_format))) # <class 'time.struct_time'>

    return time.strftime(local_format, ltime)


ret = l[0].get("time").split('.')[0]
current_time_int = utc_to_local(ret)
print(current_time_int)












