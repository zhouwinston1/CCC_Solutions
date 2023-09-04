location = input().split()
numList = [0]
ans = []
tempans = []

location = list(map(int, location))

for i in range(4):
    numList.append(numList[i] + location[i])

for i in range(5):
    r = []
    for j in range(5):
        dist = numList[j] - numList[i]
        if dist < 0:
            dist *= -1
        r.append(dist)
    print(*r)