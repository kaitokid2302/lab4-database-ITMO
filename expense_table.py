'''
CREATE TABLE IF NOT EXISTS expense(
    id SERIAL PRIMARY KEY,
    price INTEGER NOT NULL,
    _time TIMESTAMP NOT NULL UNIQUE
);
'''

import random
from datetime import datetime, timedelta

def createRow(maximumN):
    file = open('expense.sql', 'w')
    file.write('INSERT INTO expense(price, _time) VALUES\n')
    file.close()
    a = []
    dic = {}
    for i in range(maximumN):
        price = random.randint(1, 3000)
        
        # currenttime - random time between 1 and 1000 days, by now - random second
        minSecond = 24*60*60
        maxSecond = 1000*24*60*60
        second = random.randint(minSecond, maxSecond)
        _time = datetime.now() - timedelta(seconds=second)
        # year-month-date hour:minute:second
        _time_str = _time.strftime("%Y-%m-%d %H:%M:%S")
        while _time_str in dic:
            second = random.randint(minSecond, maxSecond)
            _time = datetime.now() - timedelta(seconds=second)
            _time_str = _time.strftime("%Y-%m-%d %H:%M:%S")
        
        # insert to dic
        dic[_time_str] = 1
        s = f"({price}, '{_time_str}')"
        a.append(s)
    return a
    


def genExpense(maximumN):
    a = createRow(maximumN)
    file = open('expense.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')

