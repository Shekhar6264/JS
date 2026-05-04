def valid_palindrome(s):
    s = ''.join(s.split()).lower()
    a = ''
    for i in a:
        if i.isalnum():
            a += i
    if a == a[::-1]:
        return True
    return False
s = "A man, a plan, a canal: Panama"
result = valid_palindrome(s)
print("Is the string a valid palindrome? ", result)