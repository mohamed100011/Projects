def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def muliply(n1, n2):
    return n1 * n2


operation = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": muliply,
}


def calculator():
    num1 = float(input("What's Your Frist Number "))

    for symbol in operation:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operations:  ")
        num2 = float(input("What's Your next Number "))

        functions = operation[operation_symbol]

        answer = functions(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (
            input(
                f"type 'y' if you want continue With {answer} or 'n' to a strat new calculator. "
            )
            == "y"
        ):
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
