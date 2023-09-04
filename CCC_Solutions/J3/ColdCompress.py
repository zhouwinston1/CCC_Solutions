lines = int(input())
final = []

for check in range(lines):
    answer = []
    newcheck = input()
    tempnum = 1
    templist = [str(num) for num in str(newcheck)]
    for secheck in range(len(templist)):
        if len(templist) == int(secheck + 1):
            answer.append(str(tempnum) + " " + templist[secheck] + " ")
            tempnum = 1
            break
        elif templist[secheck] == templist[secheck + 1]:
            tempnum += 1
        else:
            answer.append(str(tempnum) + " " + templist[secheck] + " ")
            tempnum = 1
    final.append(answer)

for ans in final:
    newNum = ''.join(ans)
    print(newNum)



