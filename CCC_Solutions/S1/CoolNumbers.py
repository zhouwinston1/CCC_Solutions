start = int(input())
end = int(input())

temp = 0
ans = []

for i in range(start, end+1):
    temp = i**(1/2)
    if i % temp == 0:
        temp = i**(1/3)
        if i % temp == 0:
            ans.append(i)
    else:
        continue

ans.append(64)

print(len(ans))

