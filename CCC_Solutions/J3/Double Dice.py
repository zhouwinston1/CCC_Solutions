rounds, antonio, david = int(input()), 100, 100
for round in range(rounds):
    rolls = input().split()
    if int(rolls[0]) > int(rolls[-1]):
        david -= int(rolls[0])
    elif int(rolls[0]) < int(rolls[-1]):
        antonio -= int(rolls[-1])
print(f"{antonio} \n{david}")