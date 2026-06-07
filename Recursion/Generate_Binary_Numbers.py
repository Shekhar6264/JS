def generate_binary(n,curr,result):
    if len(curr) == n:
        result.append(curr)
        return result
    generate_binary(n,curr+'0',result)
    if len(curr) == 0 or curr[-1]!='1':
        generate_binary(n,curr+'1',result)
result = []
generate_binary(3,'',result)
print(result)