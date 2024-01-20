'''
CREATE TABLE IF NOT EXISTS supply(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    wait_time INTERVAL NOT NULL,
    address TEXT NOT NULL,
    -- >= 5 minutes
    CONSTRAINT wait_Time_Check CHECK (wait_time > INTERVAL '5 minutes')
);

'''

from datetime import datetime, timedelta
import random

def randomNameOfSupply(address):
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

def createRow(maximumN):
    # open supply.sql and write the first line
    file = open('supply.sql', 'w')
    file.write('INSERT INTO supply(name, wait_time, address) VALUES\n')
    file.close()
    a = []
    for i in range(maximumN):
        name = randomNameOfSupply(False)
        address = randomNameOfSupply(True)
        # wait time between 5 minutes and 1 second and 4 hours, by second
        minSecond = 5*60 + 1
        maxSecond = 4*60*60
        second = random.randint(minSecond, maxSecond)
        wait_time = timedelta(seconds=second)
        wait_time_str = str(wait_time)
        s = f"('{name}', '{wait_time_str}', '{address}')"
        a.append(s)
    return a

def genSupply(maximumN):
    a = createRow(maximumN)
    file = open('supply.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
