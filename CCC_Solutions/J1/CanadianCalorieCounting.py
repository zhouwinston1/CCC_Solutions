burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

caloriecount = 0

if burger == 1:
    caloriecount += 461
elif burger == 2:
    caloriecount += 431
elif burger == 3:
    caloriecount += 420
else:
    caloriecount

if side == 1:
    caloriecount += 100
elif side == 2:
    caloriecount += 57
elif side == 3:
    caloriecount += 70
else:
    caloriecount

if drink == 1:
    caloriecount += 130
elif drink == 2:
    caloriecount += 160
elif drink == 3:
    caloriecount += 118
else:
    caloriecount

if dessert == 1:
    caloriecount += 167
elif dessert == 2:
    caloriecount += 266
elif dessert == 3:
    caloriecount += 75
else:
    caloriecount

print(f"Your total Calorie count is {caloriecount}.")




