print("Welcome To Python Pizza Deliveries ! ")
size = input("what Size Do You Want ? S or M Or L ").lower()

bill = 0
if size == "s":
    bill = 15
    print(f"Your Price Is {bill}")
elif size == "m":
    bill = 20
    print(f"Your Price Is {bill}")
else:
    bill = 25
    print(f"Your Price Is {bill}")

add_pepperoni = input("Do You Want pepperoni ? 'yes' or 'no' ").capitalize()
if add_pepperoni == "yes":
    bill += 3
    print(f"You Total price is {bill}")
else:
    print(f"You Total Price Is {bill}")

extra_cheese = input("Do You Want extra cheese ? 'yes' or 'no' ").capitalize()

if extra_cheese == "yes":
    bill += 5
    print(f"You Total price is {bill}")

else:
    print(f"You Total Price Is {bill}")
