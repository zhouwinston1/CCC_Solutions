total = int(input())
inputofvotes = input()

votes = str(inputofvotes.split())

totalforA = 0
totalforB = 0

for tally in range(0, len(votes)):
    if votes[tally] == "A":
        totalforA += 1
    elif votes[tally] == "B":
        totalforB += 1

if totalforA > totalforB:
    print("A")
elif totalforA < totalforB:
    print("B")
elif totalforA == totalforB:
    print("Tie")

