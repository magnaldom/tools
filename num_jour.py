# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:47:01 2020

@author: Adèle
"""


from datetime import datetime, date, timedelta


def num_jour(date):
    y = date.year
    m = date.month
    d = date.day
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    date_str = "%s-%s-%s 00:00:00" %(y,m,d)
    to_dt = datetime.strptime(date_str, DATETIME_FORMAT)
    from_dt = datetime.strptime("%s-01-01 00:00:00" %(y), DATETIME_FORMAT)
    timedelta = to_dt - from_dt
    diff_day = timedelta.days #+ float(timedelta.seconds) / 86400
    return int(diff_day + 1)

