'''
CREATE TABLE IF NOT EXISTS ingredient(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);
'''

def createRow(maximumN):
    file = open("ingredient.txt", "r")
    ingredient = file.readlines()
    file.close()
    # remove the \n in the end of each line
    for i in range(len(ingredient)):
        ingredient[i] = ingredient[i][:-1]
    count = 0
    dic = {}
    a = []
    
    s = 'INSERT INTO ingredient(name) VALUES \n'
    file = open("ingredient.sql", "w")
    file.write(s)
    file.close()
    # 1 element in the list, i
    for i in range(len(ingredient)):
        if count == maximumN:
            break
        if ingredient[i] not in dic:
            dic[ingredient[i]] = 1
            count += 1
            # insert into the sql file
            s = f"('{ingredient[i]}')"
            a.append(s)
    # 2 elements in the list, i, j, space between 2 names ingredient[i] + ' ' + ingredient[j]
    for i in range(len(ingredient)):
        if count == maximumN:
            break
        for j in range(len(ingredient)):
            if count == maximumN:
                break
            if ingredient[i] != ingredient[j]:
                if ingredient[i] + ' ' + ingredient[j] not in dic:
                    dic[ingredient[i] + ' ' + ingredient[j]] = 1
                    count += 1
                    # insert into the sql file
                    s = f"('{ingredient[i]} {ingredient[j]}')"
                    a.append(s)
    # 3 elements in the list, i, j, k, space between 3 names ingredient[i] + ' ' + ingredient[j] + ' ' + ingredient[k]
    for i in range(len(ingredient)):
        if count == maximumN:
            break
        for j in range(len(ingredient)):
            if count == maximumN:
                break
            for k in range(len(ingredient)):
                if count == maximumN:
                    break
                if ingredient[i] != ingredient[j] and ingredient[i] != ingredient[k] and ingredient[j] != ingredient[k]:
                    if ingredient[i] + ' ' + ingredient[j] + ' ' + ingredient[k] not in dic:
                        dic[ingredient[i] + ' ' + ingredient[j] + ' ' + ingredient[k]] = 1
                        count += 1
                        # insert into the sql
                        s = f"('{ingredient[i]} {ingredient[j]} {ingredient[k]}')"
                        a.append(s)
    return a

def genIngredient(maximumN):
    a = createRow(maximumN)
    file = open("ingredient.sql", "a")
    for i in range(len(a)):
        if i == len(a) - 1:
            file.write(a[i] + ';')
        else:
            file.write(a[i] + ',\n')
    file.close()
    print("Done!")

