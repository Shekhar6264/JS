def rotate_string(s, goal):
    a = s+s
    if len(s)!=len(goal):
        return False
    temp =''
    k = len(goal)
    for i in range(len(a)):
        temp = a[i:i+k]
        if temp == goal:
            return True
    return False
s = 'abcde'
goal = 'cdeab'
print(rotate_string(s,goal))
