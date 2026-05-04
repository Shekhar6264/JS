def happyNumber(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1
n = 19
result = happyNumber(n)
print("Is the number a happy number? ", result)
