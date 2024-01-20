'''

CREATE TABLE IF NOT EXISTS customer(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL,
    -- > 5 minutes
    wait_time INTERVAL NOT NULL CHECK (wait_time > INTERVAL '5 minutes')
);

'''

from datetime import datetime, timedelta
import random

def randomNameOfCustomer(address):
    if address == True:
        # 2 words, 1 space, 6 letters per word
        name = ''
        for i in range(2):
            # random a word
            word = ''
            for j in range(6):
                # random a letter
                letter = chr(random.randint(97, 122))
                word += letter
            name += word + ' '
        return name[:-1]
    # 5 letters
    name = ''
    for i in range(5):
        # random a letter
        letter = chr(random.randint(97, 122))
        name += letter
    return name

def randomPhone():
    # 8 numbers
    phone = ''
    for i in range(8):
        number = str(random.randint(0, 9))
        phone += number
    # if phone is all 0, and randomPhone() again
    if phone == '00000000':
        return randomPhone()
    return phone

def createRow(maximumN):
    file = open('customer.sql', 'w')
    file.write('INSERT INTO customer(name, phone, address, wait_time) VALUES\n')
    file.close()
    a = []
    dic = {}
    for i in range(maximumN):
        name = randomNameOfCustomer(False)
        phone = randomPhone()
        while phone in dic:
            phone = randomPhone()
        dic[phone] = 1
        address = randomNameOfCustomer(True)
        # wait time between 5 minutes and 1 second and 4 hours, by second
        minSecond = 5*60 + 1
        maxSecond = 4*60*60
        second = random.randint(minSecond, maxSecond)
        wait_time = timedelta(seconds=second)
        wait_time_str = str(wait_time)
        s = f"('{name}', '{phone}', '{address}', '{wait_time_str}')"
        a.append(s)
    return a

def genCustomer(maximumN):
    a = createRow(maximumN)
    file = open('customer.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
