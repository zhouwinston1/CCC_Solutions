amount = int(input())
f = 0
e = 0

for check in range(amount):
    line = input()
    tempList = [str(num) for num in str(line)]
    for secheck in tempList:
        if secheck == 's' or secheck == 'S':
            f += 1
        elif secheck == 't' or secheck == 'T':
            e += 1

if e>f:
    print("English")
elif e<f:
    print("French")
else:
    print("French")