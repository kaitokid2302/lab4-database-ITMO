# in this code, we will generate a row of the dish table, at least 10000 rows
# and then we will insert the data into the database
'''
CREATE TABLE IF NOT EXISTS dish(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL CHECK(price > 0 AND price <= 100),
    description TEXT NOT NULL,
    time_to_do INTERVAL NOT NULL,
    CONSTRAINT time_To_Do_Check CHECK (time_to_do > INTERVAL '5 minutes' AND time_to_do <= INTERVAL '2 hours')
);
'''

from datetime import datetime, timedelta
import random

def createRow(maximumN):
    # read dish from the file dish.txt
    file = open("dish.txt", "r")
    dish = file.readlines()
    file.close()
    #remove the \n in the end of each line
    for i in range(len(dish)):
        dish[i] = dish[i][:-1]
    count = 0
    # only one element in the list 
    s = 'INSERT INTO dish(name, price, description, time_to_do) VALUES \n'
    #write to dish.sql
    file = open("dish.sql", "w")
    file.write(s)
    file.close()

    dic = {}
    a = []
    # 1 element in the list, i
    for i in range(len(dish)):
        if count == maximumN:
            break
        if dish[i] not in dic:
            dic[dish[i]] = 1
            count += 1
            # generate price randomly between 1 and 100
            price = random.randint(1, 100)
            # generate time_to_do randomly between 6 minutes and 2 hours, using datetime format, by second
            time_to_do = random.randint(301, 2*60*60)
            time_to_do = timedelta(seconds=time_to_do)
            time_to_do_str = str(time_to_do)
            # description: This is a dish, called f'name'
            name = dish[i]
            description = f"This is a dish, called {name}"
            # insert into the sql file
            s = f"('{name}', {price}, '{description}', '{time_to_do_str}')"
            a.append(s)
    # 2 elements in the list, i, j
    for i in range(len(dish)):
        if count == maximumN:
            break
        for j in range(len(dish)):
            if count == maximumN:
                break
            if dish[i] != dish[j]:
                if dish[i] + dish[j] not in dic:
                    dic[dish[i] + dish[j]] = 1
                    count += 1
                    # generate price randomly between 1 and 100
                    price = random.randint(1, 100)
                    # generate time_to_do randomly between 6 minutes and 2 hours, using datetime format, by second
                    time_to_do = random.randint(301, 2*60*60)
                    time_to_do = timedelta(seconds=time_to_do)
                    time_to_do_str = str(time_to_do)
                    # description: This is a dish, called f'name'
                    name = dish[i] + dish[j]
                    description = f"This is a dish, called {name}"
                    # insert into the sql file
                    s = f"('{name}', {price}, '{description}', '{time_to_do_str}')"
                    a.append(s)
    # 3 elements in the list, i, j, k
    for i in range(len(dish)):
        if count == maximumN:
            break
        for j in range(len(dish)):
            if count == maximumN:
                break
            for k in range(len(dish)):
                if count == maximumN:
                    break
                if dish[i] != dish[j] and dish[i] != dish[k] and dish[j] != dish[k]:
                    if dish[i] + dish[j] + dish[k] not in dic:
                        dic[dish[i] + dish[j] + dish[k]] = 1
                        count += 1
                        # generate price randomly between 1 and 100
                        price = random.randint(1, 100)
                        # generate time_to_do randomly between 6 minutes and 2 hours, using datetime format, by second
                        time_to_do = random.randint(301, 2*60*60)
                        time_to_do = timedelta(seconds=time_to_do)
                        time_to_do_str = str(time_to_do)
                        # description: This is a dish, called f'name'
                        name = dish[i] + dish[j] + dish[k]
                        description = f"This is a dish, called {name}"
                        # insert into the sql file
                        s = f"('{name}', {price}, '{description}', '{time_to_do_str}')"
                        a.append(s)
    return a
    
def genDish(maximumN):
    a = createRow(maximumN)
    # write to dish.sql
    file = open("dish.sql", "a")
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')


