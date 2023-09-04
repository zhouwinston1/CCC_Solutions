import math

inputs = []
value = int(input())
while value != 99999:
    inputs.append(value)
    value = int(input())

outputs = []
previousDirection = ""
for num in inputs:
    firstDigit = math.floor(num / 10000)
    secondDigit = math.floor(num / 1000)
    numOfSteps = num % 1000
    if  firstDigit+secondDigit == 0:
        outputs.append(previousDirection + str(numOfSteps))
    elif (firstDigit+secondDigit) % 2 == 0:
        previousDirection = "right "
        outputs.append(previousDirection + str(numOfSteps))
    else:
        previousDirection = "left "
        outputs.append(previousDirection + str(numOfSteps))

for string in outputs:
    print(string)

