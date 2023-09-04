loops = int(input())

encoding = {}

for inputs in range(loops):
    temp = input().split()
    encoding[temp[1]] = temp[0]


text = input()
encryption = []
for t in str(text):
    encryption.append(t)

temp = []
val = 0

answer = []

while val < len(encryption):
    temp.append(encryption[val])
    testing = ''.join(temp)

    if testing in encoding:
        answer.append(encoding[testing])
        temp = []
    val += 1

print(''.join(answer))



