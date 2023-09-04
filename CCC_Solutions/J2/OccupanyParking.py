spots = int(input())
yesterdayspots = input()
todayspots = input()

amount = 0

for checkspots in range(spots):
    if yesterdayspots[checkspots] == "C" and todayspots[checkspots] == "C":
        amount += 1
    else:
        continue

print(amount)
