fences =  int(input())
sides = input().split(" ")
bases = input().split(" ")

ans = []


def formula(base, left, right):
    return base * ((left+right)/2)


for attempts in range(fences):
    ans.append(formula(int(bases[attempts]),int(sides[attempts]),int(sides[attempts+1])))

sum1 = 0

for check in ans:
    sum1 += check

print(sum1)

