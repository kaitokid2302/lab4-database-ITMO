'''
CREATE TABLE IF NOT EXISTS _order(
    id SERIAL PRIMARY KEY,
    time_delivery TIMESTAMP NOT NULL,
    time_order TIMESTAMP NOT NULL,
    status BOOLEAN NOT NULL,
    interest INTEGER NOT NULL,
    --- customer_id references and not null
    customer_id INTEGER REFERENCES customer(id) NOT NULL,
    -- constraint time_order <= current_timestamp
    CONSTRAINT time_Order_Check CHECK (time_order <= CURRENT_TIMESTAMP)
);
'''

from datetime import datetime, timedelta
import random

def createRow(maximumN):
    file = open('order.sql', 'w')
    file.write('INSERT INTO _order(time_delivery, time_order, status, interest, customer_id) VALUES\n')
    file.close()
    a = []
    for i in range(maximumN):
        # it does not need to be unique
        # time_order from 1000 days ago to now
        minSecond = 24*60*60
        maxSecond = 1000*24*60*60
        second = random.randint(minSecond, maxSecond)
        time_order = datetime.now() - timedelta(seconds=second)
        # year-month-date hour:minute:second
        time_order_str = time_order.strftime("%Y-%m-%d %H:%M:%S")
        # time_delivery no more than 2 hours after time_order
        minSecond = 1*60*60
        maxSecond = 2*60*60
        second = random.randint(minSecond, maxSecond)
        time_delivery = time_order + timedelta(seconds=second)
        # year-month-date hour:minute:second
        time_delivery_str = time_delivery.strftime("%Y-%m-%d %H:%M:%S")
        # status randomly
        status = random.randint(0, 1)
        # convert to boolean
        if status == 0:
            status = 'FALSE'
        else:
            status = 'TRUE'
        # interest randomly, between 50 to 2000
        interest = random.randint(50, 2000)
        # customer_id randomly, between 1 to 6000
        customer_id = random.randint(1, 6000)
        s = f"('{time_delivery_str}', '{time_order_str}', {status}, {interest}, {customer_id})"
        a.append(s)
    return a

def genOrder(maximumN):
    a = createRow(maximumN)
    file = open('order.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')

genOrder(10000)