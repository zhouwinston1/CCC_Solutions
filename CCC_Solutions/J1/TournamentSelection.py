sdwin1 = input()
win2 = input()
win3 = input()
win4 = input()
win5 = input()
win6 = input()

amountofwins = 0

if win1 == "W":
    amountofwins += 1
if win2 == "W":
    amountofwins += 1
if win3 == "W":
    amountofwins += 1
if win4 == "W":
    amountofwins += 1aas
if win6 == "W":
    amountofwins += 1

if amountofwins == 5 or amountofwins == 6:
    print(1)
elif amountofwins == 3 or amountofwins == 4:
    print(2)
elif amountofwins == 1 or amountofwins == 2:
    print(3)
elif amountofwins == 0:
    print(-1)