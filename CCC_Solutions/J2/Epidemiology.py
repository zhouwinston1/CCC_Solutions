P = int(input())
N = int(input())
R = int(input())

infected = N
infected_total = N
days = 0

while infected_total <= P:
    infected *= R
    infected_total += infected
    days += 1

print(days)
