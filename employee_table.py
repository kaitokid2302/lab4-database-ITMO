'''
CREATE TABLE IF NOT EXISTS employee(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL CHECK(salary > 0 AND salary <= 2000),
    status BOOLEAN NOT NULL
);
'''

import random

def createRow(maximumN):
    file = open("employee.txt", "r")
    employee = file.readlines()
    file.close()
    # remove the \n in the end of each line
    for i in range(len(employee)):
        employee[i] = employee[i][:-1]
    count = 0
    dic = {}
    a = []
    
    s = 'INSERT INTO employee(name, salary, status) VALUES \n'
    file = open("employee.sql", "w")
    file.write(s)
    file.close()
    # 1 element in the list, i
    for i in range(len(employee)):
        if count == maximumN:
            break
        if employee[i] not in dic:
            dic[employee[i]] = 1
            count += 1
            # generate salary randomly between 1 and 2000
            salary = random.randint(1, 2000)
            # generate status randomly
            status = random.choice([True, False])
            # insert into the sql file
            s = f"('{employee[i]}', {salary}, {status})"
            a.append(s)
    # 2 elements in the list, i, j, space between 2 names employee[i] + ' ' + employee[j]
    for i in range(len(employee)):
        if count == maximumN:
            break
        for j in range(len(employee)):
            if count == maximumN:
                break
            if employee[i] != employee[j]:
                if employee[i] + ' ' + employee[j] not in dic:
                    dic[employee[i] + ' ' + employee[j]] = 1
                    count += 1
                    # generate salary randomly between 1 and 2000
                    salary = random.randint(1, 2000)
                    # generate status randomly
                    status = random.choice([True, False])
                    # insert into the sql file
                    s = f"('{employee[i]} {employee[j]}', {salary}, {status})"
                    a.append(s)
    # 3 elements in the list, i, j, k, space between 3 names employee[i] + ' ' + employee[j] + ' ' + employee[k]
    for i in range(len(employee)):
        if count == maximumN:
            break
        for j in range(len(employee)):
            if count == maximumN:
                break
            for k in range(len(employee)):
                if count == maximumN:
                    break
                if employee[i] != employee[j] and employee[j] != employee[k] and employee[i] != employee[k]:
                    if employee[i] + ' ' + employee[j] + ' ' + employee[k] not in dic:
                        dic[employee[i] + ' ' + employee[j] + ' ' + employee[k]] = 1
                        count += 1
                        # generate salary randomly between 1 and 2000
                        salary = random.randint(1, 2000)
                        # generate status randomly
                        status = random.choice([True, False])
                        # insert into the sql file
                        s = f"('{employee[i]} {employee[j]} {employee[k]}', {salary}, {status})"
                        a.append(s)
    return a

def genEmployee(maximumN):
    a = createRow(maximumN)
    file = open("employee.sql", "a")
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
