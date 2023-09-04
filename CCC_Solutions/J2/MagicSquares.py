line1 = input()
line2 = input()
line3 = input()
line4 = input()

notmagic = 0

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

numbers1 = [int(num1) for num1 in line1.split(" ", 3)]
for num1 in numbers1:
    sum1 += num1
numbers2 = [int(num2) for num2 in line2.split(" ", 3)]
for num2 in numbers2:
    sum2 += num2
numbers3 = [int(num3) for num3 in line3.split(" ", 3)]
for num3 in numbers3:
    sum3 += num3
numbers4 = [int(num4) for num4 in line4.split(" ", 3)]
for num4 in numbers4:
    sum4 += num4

if sum1 == sum2 == sum3 == sum4:

    for v in range(0, 4):
        if numbers1[v] + numbers2[v] + numbers3[v] + numbers4[v] == sum1:
            continue
        else:
            notmagic += 1
            break
else:
    notmagic += 1

if notmagic == 0:
    print("magic")
else:
    print("not magic")





