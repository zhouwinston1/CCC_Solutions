amountofstr = int(input())

output = []
for check in range(amountofstr):
    line = input()
    linecheck = line.split()

    number = int(linecheck[0])
    text = linecheck[-1]
    output.append(number * text)

for texts in output:
    print(texts)
