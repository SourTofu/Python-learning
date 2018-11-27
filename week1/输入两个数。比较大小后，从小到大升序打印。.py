a = int(input('>>>'))
b = int(input('>>>'))
if a > b:
    print(b)
    print(a)
else:
    print(a)
    print(b)
#三目表达式为Ture if 条件 else falis
c = int(input('>>>'))
d = int(input('>>>'))
print(c,d) if c < d else print(d,c)