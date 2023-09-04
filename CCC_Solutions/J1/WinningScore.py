applesthree = int(input())
applestwo = int(input())
applesone = int(input())
bananasthree = int(input())
bananastwo = int(input())
bananasone = int(input())

applesscore = (applesthree * 3) + (applestwo * 2) + applesone

bananasscore = (bananasthree * 3) + (bananastwo * 2) + bananasone

if bananasscore > applesscore:
    print("B")
elif bananasscore < applesscore:
    print("A")
else:
    print("T")

