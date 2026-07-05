print("""

__   __                               _             _ _ 
\ \ / /__  _   _ _ __    ___  _ __ __| | ___ _ __  | | |
 \ V / _ \| | | | '__|  / _ \| '__/ _` |/ _ \ '__| | | |     
  | | (_) | |_| | |    | (_) | | | (_| |  __/ |    |_|_|
  |_|\___/ \__,_|_|     \___/|_|  \__,_|\___|_|    (_|_)
      
    _.:`.--|--.`:._
  .: .'\o  | o /'. '.
 // '.  \ o|  /  o '.\
//'._o'. \ |o/ o_.-'o\\
|| o '-.'.\|/.-' o   ||
||--o--o-->|<o-----o-||
\\  o _.-'/|\'-._o  o//
 \\.-'  o/ |o\ o '-.//
  '.'.o / o|  \ o.'.'
    `-:/.__|__o\:-'
       `"--=--"`

    
""")
print("-"*100)
print("Please place your sir!!!----")
print("-"*100)
print("1.Small size Pizza ")
print("-"*100)
print("2.Medium size Pizza ")
print("-"*100)
print("3.Larger size Pizza ")
bill=0
print("-"*100)
print("""

| Pizza          | Small | Medium | Large |
| -------------- | ----: | -----: | ----: |
| Margherita     |  ₹199 |   ₹299 |  ₹399 |
| Farmhouse      |  ₹249 |   ₹349 |  ₹449 |
| Veggie Supreme |  ₹269 |   ₹379 |  ₹489 |
| Pepperoni      |  ₹299 |   ₹419 |  ₹549 |
| BBQ Chicken    |  ₹329 |   ₹459 |  ₹599 |
""")
print("-"*100)
pizza=input("What type of Pizza you want :-").lower()
print("-"*100)
size=input("Choose your size:-").lower()
print("-"*100)
if pizza=="margherita":
    if size=="small":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=199
    elif size=="medium":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=299
    elif size=="larger":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=399
elif pizza=="farmhouse":
    if size=="small":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=249
    elif size=="medium":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=349
    elif size=="larger":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=449
elif pizza=="veggie supreme":
    if size=="small":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=269
    elif size=="medium":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=379
    elif size=="larger":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=489
elif pizza=="pepperoni":
    if size=="small":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=299
    elif size=="medium":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=419
    elif size=="larger":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=549
elif pizza=="bbq chicken":
    if size=="small":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=329
    elif size=="medium":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=459
    elif size=="larger":
        print(f"Your order Placed SIR!! {pizza} of size {size}")
        bill+=599
else:
    print("-"*100)
    print("You have been order worng itemm?? \n please order according to the option:!!")
    print("-"*100)
print("-"*100)
print("""
| Crust         | Extra Cost |
| ------------- | ---------: |
| Classic       |         ₹0 |
| Thin Crust    |        ₹30 |
| Cheese Burst  |       ₹100 |
| Stuffed Crust |       ₹120 |
""")
print("-"*100)
print("""Which crust do you prefer?
\n
1.Classic\n
2.Thin Crust\n
3.Cheese Burst\n
4.Stuffed Crust\n""")
print("-"*100)
crust=input("choose your crust:").lower()
if crust=="classic":
    bill+=0
elif crust=="thin crust":
    bill+=30
elif crust=="cheese burst":
    bill+=100
elif crust=="stuffed crust":
    bill+=120
print("-"*100)
print("""
| Topping      | Price |
| ------------ | ----: |
| Extra Cheese |   ₹60 |
| Mushrooms    |   ₹40 |
| Sweet Corn   |   ₹35 |
| Onions       |   ₹20 |
| Capsicum     |   ₹25 |
| Tomatoes     |   ₹20 |
| Jalapeños    |   ₹40 |
| Paneer       |   ₹70 |
| Chicken      |   ₹90 |
| Bacon        |  ₹100 |
""")
print("-"*100)
topping=input("SIR, Do you want to choose some extra (YES/NO):").lower()
print("-"*100)
if topping=="yes":
    choose=input("Please Sir! , Choose your Topping :")
    if choose=="extra cheese":
        bill+=60
    elif choose=="mushrooms":
        bill+=40
    elif choose=="sweet corn":
        bill+=35
    elif choose=="onions":
        bill+=20
    elif choose=="capsicum":
        bill+=25
    elif choose=="tomatoes":
        bill+=20
    elif choose=="jalapenos":
        bill+=40
    elif choose=="paneer":
        bill+=70
    elif choose=="chicken":
        bill+=90
    elif choose=="bacon":
        bill+=100
else:
    print("-"*100)
    print("OK Sir , !!")
    bill+=0
print("-"*100)
print("""
| Drink          | Price |
| -------------- | ----: |
| Coke (500ml)   |   ₹60 |
| Pepsi (500ml)  |   ₹60 |
| Sprite (500ml) |   ₹60 |
| Fanta (500ml)  |   ₹60 |
| Water          |   ₹20 |
""")
print("-"*100)
print("please sir choose your drink:")
print("-"*100)
drink=input("Enter your choice , sir :")
print("-"*100)
number_of_drink=int(input("enter number of drinks you want:\n----///---:"))
print("-"*100)
if drink=="coke":
    print(f"Here's your drink sir!! {drink}")
    bill+=60*number_of_drink
if drink=="pepsi":
    print(f"Here's your drink sir!! {drink}")
    bill+=60*number_of_drink
elif drink=="sprite":
    print(f"Here's your drink sir!! {drink}")
    bill+=60*number_of_drink
elif drink=="fanta":
    print(f"Here's your drink sir!! {drink}")
    bill+=60*number_of_drink
elif drink=="water":
    print(f"Here's your drink sir!! {drink}")
    bill+=20*number_of_drink
print("-"*100)
print("""
| Item                  | Price |
| --------------------- | ----: |
| French Fries          |   ₹99 |
| Garlic Bread          |  ₹129 |
| Cheese Garlic Bread   |  ₹169 |
| Chicken Wings (6 pcs) |  ₹249 |
| Nuggets (6 pcs)       |  ₹179 |
""")
print("-"*100)
option = input("Do you any side dish sir ???:").lower()
print("-"*100)
if option=="yes":
    print("-"*100)
    choice=input("Choose your side dish:").lower()
    print("-"*100)
    number_of_side_dish=int(input("Enter nno. of side dish you want:"))
    print("-"*100)
    if choice=="french fries":
        print(f"your side dish {choice}")
        bill+=99*number_of_side_dish
    elif choice=="garlic bread":
        print(f"your side dish {choice}")
        bill+=129*number_of_side_dish
    elif choice=="cheese gralic bread":
        print(f"your side dish {choice}")
        bill+=169*number_of_side_dish
    elif choice=="chicken wings":
        print(f"your side dish {choice}")
        bill+=249*number_of_side_dish
    elif choice=="nuggets":
        print(f"your side dish {choice}")
        bill+=179*number_of_side_dish
else:
    print("-"*100)
    print("OK sir !!")
    print("-"*100)
    bill+=0
print("-"*100)
print("""

| Dessert           | Price |
| ----------------- | ----: |
| Chocolate Brownie |   ₹99 |
| Ice Cream         |   ₹79 |
| Cheesecake        |  ₹159 |
      

""")
print("-"*100)

print("Please ! enter your desert sir :")
print("-"*100)
desert=input("Enter your choosen desert from the above MENU:")
print("-"*100)
if desert=="chocolate brownie":
    print(f"Your desert sir {desert}")
    bill+=99
elif desert=="ice cream":
    print(f"Your desert sir {desert}")
    bill+=79
elif desert=="cheesecake":
    print(f"Your desert sir {desert}")
    bill+=159
print("-"*100)
print("Thank you sir for Order ")
print("-"*100)
print(f"Here's your ordered list : {pizza} with {size} size and your total billis :{bill}")
print("-"*100)


