inp = int(input())
mins = 0
hrs = 12

temp = []
str_temp1 = ""
str_temp2 = ""

total = 0
for i in range(inp):
    str_temp1 = str(hrs)
    str_temp2 = str(mins)

    for item in str_temp1:
        temp.append(item)
    for item in str_temp2:
        temp.append(item)

    if len(temp) == 3:
        if int(temp[0]) - int(temp[1]) == int(temp[1]) - int(temp[2]):
            total += 1

    # elif len(temp) == 4:
    #     if int(temp[0]) - int(temp[1]) == int(temp[1]) - int(temp[2]) == int(temp[2]) - int(temp[3]):
    #         total += 1

    if mins == 59:
        mins = 0
        if hrs == 12:
            hrs = 1
        else:
            hrs += 1
    else:
        mins += 1
    temp = []

print(total)
