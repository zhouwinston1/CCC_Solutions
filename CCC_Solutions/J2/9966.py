start = int(input())
end = int(input())
amount = 0

for numbercheck in range(start, end + 1):
    flipped = ""
    skip = False
    number = str(numbercheck)

    for numberswitch in range(len(number)):
        if number[numberswitch] == "6":
            flipped += "9"
        elif number[numberswitch] == "1":
            flipped += "1"
        elif number[numberswitch] == "9":
            flipped += "6"
        elif number[numberswitch] == "0":
            flipped += "0"
        elif number[numberswitch] == "8":
            flipped += "8"
        else:
            skip = True
            break

    if number == flipped[::-1] and skip == False:
        amount += 1

print(amount)
