""" Pizza Order Calculator
Kennedy Walker
Date: 9/18/2026
Reason: This program is to calculate the prcie of the pizza after the customer orders"""

print ("Welcome to Kennedy's Pizza")

# Using if, elif, then statement to add price for the size of the pizza
size = input ("What size pizza would you like? Small, Medium, or Large")

if size == "Small":
    price = 10
elif size == "Medium":
     price = 12
elif size == "Large":
    price = 15
else:
     print ("Sorry that is not an option")

#Adding toppin choice using a List
toppings = [ "Cheese only", "Pepperponi", "Sausauge", "Bacon"]
print ("The availble toppings are :",toppings )
choice = input("Select one topping you would like for your Pizza")
#adding price of toppings 
 if choice == "Cheese only":
    with_topping =0
else:
with_topping = 2
