# Updated Code to handle iterating over all list of items in menu with For loop,

# And to handle user choice, price total calculation and if user want to continue 
# further with order, with While loop


menu = {
   "pasta": 50,
   "pizza": 80,
   "noddles": 90,
   "salad": 60,
   "burger": 120,
   "thukpa": 50,
   "beg momo": 70,
   "chicken momo": 160,
   "chicken chilli": 150,
   "chocolate pestries": 160,
   "black forest pestries": 120,
   "cold drink": 55,
   "cold coffee": 115,
   "hot coffee": 105,
}




print("Welcome to KAVYA Bakery & Restaurant")


for item_key, item_value in menu.items():
   print(f"{item_key}: Rs.{item_value}")


order_total = 0


continue_ordering = True


while continue_ordering:
   item = input("Enter the name of item you want to order =")
   item = item.lower()
   if item in menu:
       order_total += menu[item]
       print(f"your item {item} has been added to your order")
   else:
       print(f"Ordered item {item} is not available yet!")
   continue_ordering = input("Do you want to add another item? (Yes/No) ") == "Yes"


print(f"The total amount of item to pay is {order_total}")








