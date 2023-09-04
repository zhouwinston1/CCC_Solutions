num = int(input())
div = int(input())
found = False
ans = 0
for i in range(div):
    if (num * i) % div == 1:
        found = True
        ans = i
        break
if found:
    print(ans)
else:
    print("No such integer exists.")