def longest_prefix(s):
    ans = ''
    smallest = min(s)
    lon = max(s)
    i = 0
    while i < len(s):
        if smallest[i] == lon[i]:
            ans += smallest[i]
        else:
            break
        i += 1
    return ans
s = ["flower", "flow", "flight"]
result = longest_prefix(s)
print("Longest common prefix: ", result)