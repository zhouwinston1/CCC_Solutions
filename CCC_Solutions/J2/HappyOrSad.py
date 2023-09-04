emoji = input()

happy = emoji.count(":-)")
sad = emoji.count(":-(")

if sad > happy:
    print("sad")
elif happy > sad:
    print("happy")
elif happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")