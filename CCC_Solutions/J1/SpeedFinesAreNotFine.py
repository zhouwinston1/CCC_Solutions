speedlimit = int(input())
speedofcar = int(input())

speedingcheck = speedofcar - speedlimit

if 20 >= speedingcheck >= 1:
    print("You are speeding and your fine is $100.")
elif 30 >= speedingcheck >= 21:
    print("You are speeding and your fine is $270.")
elif speedofcar <= speedlimit:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is $500.")

