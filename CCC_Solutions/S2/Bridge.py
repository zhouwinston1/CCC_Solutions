maxweight = int(input())
totalcars = int(input())
train =[]

for i in range(totalcars):
    train.append(int(input()))

carscanpass = 0
if train[0] <= maxweight:
    carscanpass += 1
if train[0]+train[1] <= maxweight:
    carscanpass += 1
if train[0]+train[1] + train[2] <= maxweight:
    carscanpass += 1
for i in range(len(train)-3):
    if train[i] + train[i+1] + train[i+2] + train[i+3] <= maxweight:
        carscanpass += 1
    else:
        break

print(carscanpass)
