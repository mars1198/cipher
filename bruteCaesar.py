alpha = 'abcdefghijklmnopqrstuvwxyz'

s = input().strip()
n=0
while n<24:
    res = ''
    for c in s:
        res += alpha[(alpha.index(c) - n) % len(alpha)]
    print('Result: "' + res + '"')
    n+=1
