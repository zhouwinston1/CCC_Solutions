runs = int(input())

responses = []
answers = []

for student in range(runs):
    responses.append(input())

for ans in range(runs):
    answers.append(input())

correct = 0

for checking in range(len(answers)):
    if responses[checking] == answers[checking]:
        correct += 1

print(correct)