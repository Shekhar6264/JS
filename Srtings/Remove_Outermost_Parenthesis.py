def parenthesis(s):
    count = 0
    ans = ''
    for i in s:
        if i == '(':
            if count > 0:
                ans += i
            count += 1
        else:
            count -= 1
            if count > 0:
                ans += i
    return ans
s = "(()())(())"
result = parenthesis(s)
print("String after removing outermost parentheses: ", result)