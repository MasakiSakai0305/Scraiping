#国際興業バス限定
#時刻表のurlが別途必要

import requests
from bs4 import BeautifulSoup
from datetime import datetime


# 今日の曜日・時間帯を取得
def get_date():

    week = datetime.today().weekday()
    hour = datetime.today().hour
    minute = datetime.today().minute

    # 平日
    if week >= 0 and week <= 4:
        day = 'wkd'

    # 土曜日
    elif week == 5:
        day = 'std'

    # 日曜日
    else:
        day = 'snd'

    print('現在: ' + str(hour) + '時' + str(minute) + '分')

    return day, hour, minute

def get_bus_tag(url, hour):
    hours = []
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    bs = BeautifulSoup(response.text, 'html.parser')

    #HTMLの中から時刻表のタグを入手
    table_list = bs.find(class_='diagram-table parallel')
    table_list = bs.find_all(class_='l2')

    for bus_time in table_list:
        hours.append(bus_time)

    #現在時刻、現在時刻+1時間のタグを入手
    hours_now = hours[hour - 5]
    hours_add = hours[hour - 4]

    return hours_now, hours_add

def get_bus_time(day, hours, hours_add):

    times, times_add = [], []
    hour = datetime.today().hour

    days = hours.find(class_=day)
    days_add = hours_add.find(class_=day)

    days = days.find_all('a')
    days_add = days_add.find_all('a')

    # 今の時刻の ~ +1の範囲で時刻を表示
    print(str(hour) + '時')
    for day_time in days:
        times.append(day_time.text.strip())
    print(times)

    print(str(hour + 1) + '時')
    for day_plu_time in days_add:
        times_add.append(day_plu_time.text.strip())
    print(times_add)


