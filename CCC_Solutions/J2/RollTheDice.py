dice1 = int(input())
dice2 = int(input())
amount = 0
for num1 in range(1, dice1+1):
    for num2 in range(1, dice2+1):
        if num1 + num2 == 10:
            amount += 1
if amount == 1:
    print(f"There is {amount} way to get the sum 10.")
else:
    print(f"There are {amount} ways to get the sum 10.")
