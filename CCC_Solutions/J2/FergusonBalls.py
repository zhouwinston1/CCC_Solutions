players = int(input())
stars = 0

for players in range(players):
    players = int(input())
    fouls = int(input())
    if (players * 5) - (fouls * 3) > 40:
        stars += 1

if stars == numofplayers:
    print(f"{goldstars}+")

else:
    print(goldstars)    