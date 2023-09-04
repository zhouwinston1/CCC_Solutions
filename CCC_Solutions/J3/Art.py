coords = int(input())

x = []
y = []

for i in range(coords):
    temp = input().split(",")
    tempx = temp[0]
    tempy = temp[-1]
    x.append(int(tempx))
    y.append(int(tempy))

print(f"{min(x)-1},{min(y)-1}")
print(f"{max(x)+1},{max(y)+1}")