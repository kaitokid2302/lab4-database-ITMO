'''
CREATE TABLE IF NOT EXISTS supply_ingredient(
    id SERIAL PRIMARY KEY,
    supply_id INTEGER REFERENCES supply(id) NOT NULL,
    ingredient_id INTEGER REFERENCES ingredient(id) NOT NULL,
    -- price > 0 <= 90
    price INTEGER NOT NULL CHECK (price > 0 AND price <= 90)
);
'''

import random

def createRow(maximumN):
    file = open('supply_ingredient.sql', 'w')
    file.write('INSERT INTO supply_ingredient(supply_id, ingredient_id, price) VALUES\n')
    file.close()
    a = []
    dic = {}
    for i in range(maximumN):
        supply_id = random.randint(1, 10000)
        ingredient_id = random.randint(1, 10000)
        while (supply_id, ingredient_id) in dic:
            supply_id = random.randint(1, 10000)
            ingredient_id = random.randint(1, 100)
        dic[(supply_id, ingredient_id)] = 1
        price = random.randint(1, 90)
        s = f"({supply_id}, {ingredient_id}, {price})"
        a.append(s)
    return a

def genSupply_Ingredient(maximumN):
    a = createRow(maximumN)
    file = open('supply_ingredient.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
    file.close()
genSupply_Ingredient(10000)