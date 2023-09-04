humidity = int(input())
maxTime = int(input())

time = 1

a = -6 * time * time * time * time + humidity * time * time * time + 2 * time * time + time

while time <= maxTime and a > 0:
    time += 1
    a = -6 * time * time * time * time + humidity * time * time * time + 2 * time * time + time

if a > 0:
    print("The balloon does not touch ground in the given time.")

else:
    print("The balloon first touches ground at hour:")
    print(time)

