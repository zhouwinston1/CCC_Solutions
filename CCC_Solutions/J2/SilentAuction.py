numberofbids = int(input())
winner = ""
highestbid = 0

for winnercheck in range(numberofbids):
    name = input()
    bid = int(input())

    if bid > highestbid:
        winner = name
        highestbid = bid

    else:
        continue


print(winner)

