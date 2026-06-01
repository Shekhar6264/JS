def reversewords(s):
    return ' '.join(s.split()[::-1])
s = "the sky is blue"
print(reversewords(s))