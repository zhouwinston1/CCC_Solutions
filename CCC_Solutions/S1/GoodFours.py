import math

num = int(input())

counter = math.floor(num/20)
temp = num%20

run = True

if num%20 == 0:
    run = False
    counter += 1

else:
    for i in range(4):
        for j in range(5):
            if (5*i) + (4*j) == temp:
                counter += 1
                break

print(counter)