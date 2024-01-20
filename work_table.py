'''
CREATE TABLE IF NOT EXISTS work(
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id) NOT NULL,
    time_end TIMESTAMP NOT NULL,
    time_start TIMESTAMP NOT NULL,
    order_id INTEGER REFERENCES _order(id) NOT NULL,
    dish_id INTEGER REFERENCES dish(id) NOT NULL,
    -- constraint time_start <= current_timestamp and time_start <= time_end
    CONSTRAINT time_Start_Check CHECK (time_start <= CURRENT_TIMESTAMP AND time_start <= time_end)
);
'''

from datetime import datetime, timedelta
import random

def createRow(maximumN):
    file = open('work.sql', 'w')
    file.write('INSERT INTO work(employee_id, time_end, time_start, order_id, dish_id) VALUES\n')
    file.close()
    a = []
    for i in range(maximumN):
        # between 1 and 10000
        employee_id = random.randint(1, 10000)
        # between 1 and 10000
        order_id = random.randint(1, 10000)
        # between 1 and 10000
        dish_id = random.randint(1, 10000)
        # time_start from 1000 days ago to now
        minSecond = 24*60*60
        maxSecond = 1000*24*60*60
        second = random.randint(minSecond, maxSecond)
        time_start = datetime.now() - timedelta(seconds=second)
        # year-month-date hour:minute:second
        time_start_str = time_start.strftime("%Y-%m-%d %H:%M:%S")
        # time_end from time_start to maximum 2 hours after time_start
        minSecond = 1*60*60
        maxSecond = 2*60*60
        second = random.randint(minSecond, maxSecond)
        time_end = time_start + timedelta(seconds=second)
        # year-month-date hour:minute:second
        time_end_str = time_end.strftime("%Y-%m-%d %H:%M:%S")
        s = f"({employee_id}, '{time_end_str}', '{time_start_str}', {order_id}, {dish_id})"
        a.append(s)
    return a

def genWork(maximumN):
    a = createRow(maximumN)
    file = open('work.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')

