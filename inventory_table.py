'''
CREATE TABLE IF NOT EXISTS inventory(
    ingredient_id INTEGER REFERENCES ingredient(id),
    quantity INTEGER NOT NULL CHECK(quantity > 0)
);
'''
import random

def createRow(limitId, maximumN):
    # open inventory.sql
    file = open("inventory.sql", "w")
    s = 'INSERT INTO inventory(ingredient_id, quantity) VALUES \n'
    file.write(s)
    file.close()
    # writing random number between 1 and limitId, with maximumN rows, all unique
    # a = 1 to limitId
    a = []
    for i in range(1, limitId + 1):
        a.append(i)
    # take any number from a, then remove it from a
    result = []
    for i in range(maximumN):
        index = random.randint(0, len(a) - 1)
        ingredient_id = a[index]
        a.pop(index)
        # generate quantity randomly between 1 and 1000
        quantity = random.randint(1, 1000)
        # string (ingredient_id, quantity) to result
        s = f"({ingredient_id}, {quantity})"
        result.append(s)
    return result

def genInventory(limitId, maximumN):
    a = createRow(limitId, maximumN)
    # write to inventory.sql
    file = open("inventory.sql", "a")
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
        
