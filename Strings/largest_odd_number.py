def largest_odd(s):
    for i in range(len(s)-1,-1,-1):
        a = int(s[i])
        if a%2==1:
            return s[:i+1]
print(largest_odd('3643656'))