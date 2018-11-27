def s_um(a=0,b=0,c=10):
    a = 0
    b = 0
while True:
    c = int(input('>>>'))
    if c == 'quit':
        break
    a += 1
    b += c
    d = b / a
    print(d)
print(s_um())




