def parenthisis(s):
    count = 0
    res = []
    for ch in s:
        if ch == '(':
            if count > 0:
                res.append(ch)
            count += 1
        else:
            count -= 1
            if count > 0:
               res.append(ch)
    return "".join(res)
print(parenthisis(s='(()()()()())'))