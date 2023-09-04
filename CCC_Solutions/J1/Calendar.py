weekday, dayofthemonth = (input()).split()

weekday = int(weekday)
dayofthemonth = int(dayofthemonth)

print("Sun Mon Tue Wed Thr Fri Sat")

start = 1

week1 = []
week2 = []
week3 = []
week4 = []
week5 = []

for firstweek in range(1,):
    week1.append(firstweek)
for secondweek in range(7 - weekday,):
    week1.append(firstweek)
for thirdweek in range(14 - weekday,):
    week1.append(firstweek)
for fourthweek in range(21 - weekday,):
    week1.append(firstweek)
for fifthweek in range(28 - weekday,):
    week1.append(firstweek)


