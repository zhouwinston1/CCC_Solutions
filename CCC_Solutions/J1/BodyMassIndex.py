weight = float(input())
height = float(input())

bodymassindex = weight / (height * height)

if bodymassindex > 25:
    print("Overweight")
elif 25 > bodymassindex > 18.5:
    print("Normal weight")
else:
    print("Underweight")
