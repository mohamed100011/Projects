row1 = ["*", "*", "*"]
row2 = ["*", "*", "*"]
row3 = ["*", "*", "*"]


maps = [row1, row2, row3]

position = input("Where do you want to put the treaurs ")


horizonal = int(position[0])
vertical = int(position[1])

rows = maps[vertical - 1][horizonal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")
