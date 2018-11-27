a = int(input('>>>'))
while True:
    b = int(input('>>>'))
    if a >=b:
        print(a)
    elif a<=b:
        print(b)
        a = b
#A值保持不变 A和B比较，当A大时则输出A进入下次循环。反之输出B，B值代入A值。