'''
CREATE TABLE IF NOT EXISTS dish_ingredient(
    id SERIAL PRIMARY KEY,
    dish_id INTEGER REFERENCES dish(id) NOT NULL,
    ingredient_id INTEGER REFERENCES ingredient(id) NOT NULL,
    -- quantity > 0 <= 5
    quantity INTEGER NOT NULL CHECK (quantity > 0 AND quantity <= 5)
);
'''

import random

def createRow(maximumN):
    file = open('dish_ingredient.sql', 'w')
    file.write('INSERT INTO dish_ingredient(dish_id, ingredient_id, quantity) VALUES\n')
    file.close()
    a = []
    dic = {}
    for i in range(maximumN):
        dish_id = random.randint(1, 10000)
        ingredient_id = random.randint(1, 10000)
        while (dish_id, ingredient_id) in dic:
            dish_id = random.randint(1, 10000)
            ingredient_id = random.randint(1, 100)
        dic[(dish_id, ingredient_id)] = 1
        quantity = random.randint(1, 5)
        s = f"({dish_id}, {ingredient_id}, {quantity})"
        a.append(s)
    return a

def genDish_Ingredient(maximumN):
    a = createRow(maximumN)
    file = open('dish_ingredient.sql', 'a')
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
    file.close()
genDish_Ingredient(10000)