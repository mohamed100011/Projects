def prime_number(number):

    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"The is a prime number")
    else:
        print(f"The is not a prime number")


num = int(input("Write Prime Number : "))

prime_number(number=num)
