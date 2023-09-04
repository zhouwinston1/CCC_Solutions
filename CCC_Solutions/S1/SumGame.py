length = int(input())
inp1 = input().split(" ")
inp2 = input().split(" ")
temp = 0
max = 0
total1 = 0
total2 = 0
for check in range(length):
    total1 += int(inp1[check])
    total2 += int(inp2[check])
    if total1 == total2:
        temp += 1
        max = temp
    else:
        temp += 1
print(max)
