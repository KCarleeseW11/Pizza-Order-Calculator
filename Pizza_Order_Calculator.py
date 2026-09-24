""" Pizza Order Calculator
Kennedy Walker
Date: 9/18/2026
Reason: This program is to calculate the price of the pizza after the customer orders"""

print ("Welcome to Kennedy's Pizza Shop")


size = input ("What size pizza would you like? Small, Medium, or Large")

#Used "While" Loop
while size != "Small" and size != "Medium" and size != "Large" :
    print("That is not an option")
    # Using if, elif, then statement to add price for the size of the pizza
if size == "Small":
    price = 10
elif size == "Medium":
     price = 12
elif size == "Large":
    price = 15 
      
#Adding toppin choice using a List
toppings = [ "Cheese only", "Pepperponi", "Sausauge", "Bacon"]
print ("The availble toppings are :",toppings )
choice = input("Select one topping you would like for your Pizza")
#adding price of toppings 

if choice == "Cheese only":
    with_topping =0
else:
    with_topping = 2

final_price = price + with_topping
print (" The final cost of your order will be :$", final_price)