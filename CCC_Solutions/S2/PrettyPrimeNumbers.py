def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


ans = []

for i in range(int(input())):
    num = int(input())
    num2 = num

    while True:
        if is_prime(num) and is_prime(num2):
            ans.append([num, num2])
            break
        num += 1
        num2 -= 1

for item in ans:
    print(item[0], item[1])