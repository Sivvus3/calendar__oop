# days to birthday
from collections import Counter
from datetime import date, timedelta, datetime


def get_days_to_birthday(month, day, year):
    birthday_dt = date(year, month, day)
    delta = birthday_dt - date.today()

    return delta.days


# print(get_days_to_birthday(2, 4, 2023))


def get_day_name(amount):
    today = date.today()
    delta = timedelta(days=amount)

    desired_date = today + delta

    return desired_date.strftime('%A')


# print(get_day_name(get_days_to_birthday(2, 4, 2023)))


def get_time_to_eves(desired_date):
    now = datetime.now()
    delta = datetime.strptime(desired_date, '%d.%m.%Y %H:%M') - now

    return delta


# print(get_time_to_eves('24.12.2022 15:47'))


# 18.03.1985
def most_often_bd_day(bd_date):
    day, month, year = [int(x) for x in bd_date.split('-')]
    days = []

    for delta in range(100):
       dt = date(year + delta, month, day)
       days.append(dt.strftime('%A'))

    return days

days_list = most_often_bd_day('18-03-1985')



print(Counter(days_list))


