t1 = int(input())
t2 = int(input())

len = 2

temp = 0

while True:
    len += 1
    temp = t1 - t2

    if temp > t2:
        print(len)
        break
    else:
        t1 = t2
        t2 = temp

