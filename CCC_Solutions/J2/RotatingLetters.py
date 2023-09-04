text = input()
checking = True
goodletters = ["I", "O", "S", "H", "Z", "X", "N"]
for check in range(len(text)):
    if text[check] not in goodletters:
        print("NO")
        break
if checking:
    print("YES")