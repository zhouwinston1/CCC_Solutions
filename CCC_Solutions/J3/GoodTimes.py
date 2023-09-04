ottawa = int(input())

victoria = 0
edmonton = 0
winnipeg = 0
toronto = ottawa
halifax = 0
johns = 0

if ottawa - 300 < 0:
    victoria = 2400 - ottawa
else:
    victoria = ottawa - 300

if ottawa - 200 < 0:
    edmonton = 2400 - ottawa
else:
    edmonton = ottawa - 200

if ottawa - 100 < 0:
    winnipeg = 2400 - ottawa
else:
    winnipeg = ottawa - 100

if ottawa + 100 > 2400:
    halifax = 100 + (ottawa - 2400)
else:
    halifax = ottawa - 100

if ottawa + 130 > 2400:
    johns = 130 + (ottawa - 2400)
else:
    johns = ottawa + 130

print(f"{ottawa} in Ottawa")
print(f"{victoria} in Victoria\n{edmonton} in Edmonton\n{winnipeg} in Winnipeg")
print(f"{ottawa} in Toronto\n{halifax} in Victoria\n{johns} in St. John's")
