'''
gen:
supply_ingredient
Dish
Employee
Ingredient
supply
Customer
Order
dish_ingredient
Order_dish
'''

''' 
import: Order_dish_table.py
customer_table.py
dish_table.py
dish_ingredient_table.py
employee_table.py
expense_table.py
ingredient_table.py
inventory_table.py
order_table.py
supply_table.py
supply_ingredient_table.py
'''

from supply_ingredient_table import genSupply_Ingredient
from dish_table import genDish
from employee_table import genEmployee
from ingredient_table import genIngredient
from supply_table import genSupply
from customer_table import genCustomer
from order_table import genOrder
from dish_ingredient_table import genDish_Ingredient
from Order_dish_table import genOrder_Dish

def main():
    genSupply_Ingredient(10000)
    genDish(10000)
    genEmployee(10000)
    genIngredient(10000)
    genSupply(10000)
    genCustomer(10000)
    genOrder(10000)
    genDish_Ingredient(10000)
    genOrder_Dish(10000)

if __name__ == '__main__':
    main()
