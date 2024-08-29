year = int(input("Which Year do you want to check? "))


if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:

            print("leap year")

        else:
            print("Not leap year")
    else:
        print("Leep year.")
else:
    print("Not a Leep year.")
