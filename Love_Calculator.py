print("Wlecome To Love Calcultor. ")
name1 = input("what is First Name ")
name2 = input("What is their Name ")

name3 = name1 + name2

t = name3.count("t")
r = name3.count("r")
u = name3.count("u")
e = name3.count("e")

true = t + r + u + e


l = name3.count("l")
o = name3.count("o")
v = name3.count("v")
e = name3.count("e")

love = l + o + v + e


love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your Love Score Is {love_score} , you go like coca and mentos")

elif (love_score >= 40) and (love_score <= 50):
    print(f"Your Love Score Is {love_score} , you are alright together")

else:
    print(f"Your Love Score Is {love_score}")
