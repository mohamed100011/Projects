height = float(input("What Are You Height ? "))

bill = 0

if height >= 120:
    print("You Can Ride")
    age = int(input("What Are You Age ? "))
    if age < 12:
        bill = 5
        print(f"Your tickets is {bill}")
    elif age <= 18:
        bill = 7
        print(f"Your tickets is {bill}")
    else:
        bill = 12
        print(f"Your tickets is {bill}")
    photo = input("Do You Have a Photo Type 'Yes' Or 'No' ").lower()
    if photo == "yes":
        bill += 3
        print(f"Your Paid {bill}")
    else:
        print(f"You paid a just ticket {bill}")
else:
    print("You Can't Ride")
