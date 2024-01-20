'''
CREATE TABLE IF NOT EXISTS order_dish(
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES _order(id) NOT NULL,
    dish_id INTEGER REFERENCES dish(id) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0)
);
'''

import random

def createRow(maximumN):
    file = open('order_dish.sql', 'w')
    file.write('INSERT INTO order_dish(order_id, dish_id, quantity) VALUES\n')
    file.close()
    a = []
    dic = {}
    for i in range(maximumN):
        order_id = random.randint(1, 10000)
        dish_id = random.randint(1, 10000)
        while (order_id, dish_id) in dic:
            order_id = random.randint(1, 10000)
            dish_id = random.randint(1, 100)
        dic[(order_id, dish_id)] = 1
        quantity = random.randint(1, 5)
        s = f"({order_id}, {dish_id}, {quantity})"
        a.append(s)
    return a

def genOrder_Dish(maximumN):
    a = createRow(maximumN)
    file = open('order_dish.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
    file.close()
genOrder_Dish(10000)