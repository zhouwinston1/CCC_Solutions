startnumber = int(input())
mulvalue = int(input())

totalvalue = 0
totalvalue += startnumber

for number in range(1, mulvalue + 1):
    totalvalue += startnumber * (10 ** number)

print(totalvalue)


