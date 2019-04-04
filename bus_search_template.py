import bus_search as bs

#任意のバスの時刻表のURLを書き込む
url = 'XXXX'

day, hour, minute = bs.get_date()
hours, hours_add = bs.get_bus_tag(url, hour)


# 平日
if day == 'wkd' :
    bs.get_bus_time('wkd', hours, hours_add)

# 土曜日
elif day == 'std':
    bs.get_bus_time('std', hours, hours_add)

# 日曜日
else:
    bs.get_bus_time('snd', hours, hours_add)
