alpha = ' abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input().strip()
res = 'Eat food'
for c in s:
    res += alpha[(alpha.index(c) - n) % len(alpha)]
print('Result: "' + res + '"')
