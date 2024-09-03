alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

########################### encrypt function #################################

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")


################################## decrypt function ############################

# def decrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The decode text is {cipher_text}")


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)


def caeser(plain_text, shift_amount, dir):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if dir == "encode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        elif dir == "decode":
            new_position = position - shift_amount
            cipher_text += alphabet[new_position]

    print(f"The {dir} text is {cipher_text}")


should_contine = True

while should_contine:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caeser(plain_text=text, shift_amount=shift, dir=direction)

    end = input("type 'yes' if you want to go again,  Otherwise type 'no' ? ")

    if end == "no":
        should_contine = False
        print("Good Bye")
