amount = int(input())

for i in range(amount):
    print("*" * amount + "x" * amount + "*" * amount)

for i in range(amount):
    print(" " * amount + "x" * amount + "x" * amount)

for i in range(amount):
    print("*" * amount + " " * amount + "*" * amount)