people = int(input())
rounds = int(input())
counter = 0
peopleList = []
ans = []
finalans = []

for insert in range(people):
    counter += 1
    peopleList.append(counter)

for runs in range(rounds):
    multiple = int(input())
    if runs == 0:
        tempList = peopleList.copy()
    else:
        tempList = ans.copy()
        ans = []
    for loop in range(len(tempList)):
        if (tempList.index(tempList[loop])+1) % multiple != 0 or (loop == 0 and multiple != 0):
            ans.append(tempList[loop])
    finalans.append(ans)

printans = finalans[-1]

for loop in printans:
    print(loop)

