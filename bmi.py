height = float(input("Enter Your Height ? "))
weight = float(input("Enter Your Weight ? "))


bmi = round(weight / height**2)


if bmi < 18.5:
    print(f"Your Bmi Is {bmi} , Underweight")
elif bmi < 25:
    print(f"Your Bmi Is {bmi} , You Have a Normal Weight ")
elif bmi < 30:
    print(f"Your Bmi Is {bmi} , You Are Overweight ")
elif bmi < 35:
    print(f"Your Bmi Is {bmi} , You Are Obese ")
else:
    print(f"Your Bmi Is {bmi} , You Are Clinically Obese ")
