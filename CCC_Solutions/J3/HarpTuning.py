inputString = input()
chars = list(inputString)

answers = []
tempLetterList = []
tempNumberList = []
tuning = ""
num = 0

run = True

for char in chars:
    if char.isupper():
        tempLetterList.append(char)
        if len(tempLetterList) == 1 and run:
            run = False
        else:
            run = True
        continue
    elif char == '+':
        tuning = " tighten "
    elif char == '-':
        tuning = " loosen "
    else:
        tempNumberList.append(char)

    if run:
        answerString = []
        answerInt = []
        for letter in tempLetterList:
            answerString.append(letter)
        for number in tempNumberList:
            answerInt.append(number)
        answers.append("".join(answerString) + tuning + "".join(answerInt))
        tempLetterList = []
        tempNumberList = []
        run = False

for ans in answers:
    print(ans)