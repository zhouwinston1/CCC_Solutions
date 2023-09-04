length = int(input())
ans = []
temp = 0
for check in range(length):
    newNum = int(input())
    if newNum == 0:
        ans.pop(-1)
    else:
        ans.append(newNum)

sum = 0
for new in ans:
    sum += new

print(sum)