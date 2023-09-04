length = int(input())
ans = [0]
temp = []
name = ""
t = []

r = 0

for i in range(length):
    line = input().split()
    temp.append(line)
    r = int(line[1])
    s = int(line[2])
    d = int(line[3])
    calculation = (2*r)+(3*s)+d
    if max(ans) < calculation:
        name = line[0]
        r = i
        ans.append(int(calculation))
    elif max(ans) == calculation:
        t.append(name)
        t.append(line[0])
        t.sort()
        print(t)
        print(t[0], line[0])
        if t[0] == line[0]:
            name = line[0]
            t.clear()
            ans.append(int(calculation))
            r = i
            print(name)
        else:
            t.clear()
            ans.append(int(calculation))
            print("bruh")

ans.remove(0)
print(temp)
temp.pop(r)
print(temp)
ans2 = [0]
name2 = ""

for i in temp:
    r2 = int(i[1])
    s2 = int(i[2])
    d2 = int(i[3])
    calculation2 = (2*r2)+(3*s2)+d2
    if max(ans2) < calculation2:
        name2 = i[0]
        ans2.append(int(calculation2))
    elif max(ans) == calculation2:
        t.append(name2)
        t.append(i[0])
        t.sort()
        if t[0] == i[0]:
            name2 = i[0]
            t.clear()
            ans2.append(int(calculation2))
        else:
            t.clear()
            ans2.append(int(calculation2))
print(name)
print(name2)