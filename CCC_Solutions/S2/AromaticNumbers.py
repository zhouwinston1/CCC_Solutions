roman = input()

decrypt = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

ans = 0
temp = 0
val = 0
prev = 0

for text in roman:
    val += 1
    if text.isnumeric():
        temp = int(text)
    else:
        if int(decrypt[text]) >= temp:
            ans += int(decrypt[text]) * temp
            # print(f"{int(decrypt[text])} * {temp}")
        elif int(decrypt[text]) < temp and text != roman[val-3]:
            ans -= int(decrypt[text]) * temp
            # print(f"{int(decrypt[text])} * {temp} * - 1")
        elif int(decrypt[text]) < temp and text == roman[val-3]:
            ans += (prev * 2) - int(decrypt[text]) * temp
            # print(f"{prev} * 2 - {int(decrypt[text])} * {temp}")
        prev = int(decrypt[text]) * temp

        temp = 0
        # print(text, roman[val-3])
        # print(ans)

print(ans)



