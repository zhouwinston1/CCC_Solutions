userinput = input()
maxlen = 0

for lcheck in range(0, len(userinput) + 1):
    for pcheck in range(0, len(userinput) + 1):
        palindrome = userinput[lcheck:pcheck]

        if palindrome == palindrome[::-1]:
            if len(palindrome) > maxlen:
                maxlen = len(palindrome)

print(maxlen)