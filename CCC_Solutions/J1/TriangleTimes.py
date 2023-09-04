angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

allangles = angle1 + angle2 + angle3

if angle1 == angle2 == angle3 and allangles == 180:
    print("Equilateral")
elif (angle1 == angle2 or angle1 == angle3 or angle2 == angle3) and allangles == 180:
    print("Isosceles")
elif allangles == 180 and angle1 != angle2 != angle3:
    print("Scalene")
elif allangles != 180:
    print("Error")
