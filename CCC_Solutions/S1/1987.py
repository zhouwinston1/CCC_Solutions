text = int(input()) + 1
numList = [str(num) for num in str(text)]
found = False
while not found:
    dup = [x for i, x in enumerate(numList) if i != numList.index(x)]
    if len(dup) > 0:
        text += 1
        numList = [str(num) for num in str(text)]
    else:
        print(text)
        found = True


