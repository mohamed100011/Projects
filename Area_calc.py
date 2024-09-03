import math


def panit_calc(height, weight, cover):

    area = height * weight
    num_of_can = math.ceil(area / cover)

    print(f"You Need {num_of_can} cans")


test_h = int(input("Height of wall : "))
test_w = int(input("Weight of wall : "))
coverage = 5


panit_calc(height=test_h, weight=test_w, cover=coverage)
