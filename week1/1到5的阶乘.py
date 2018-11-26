#计算阶乘
while True:
    number = int(input("Pless Number:"))
    a = 1
    b = 0
    for i in range(1,number+1):
        b = a * i
        a = b
    print(str(number)+" "+str("Factorial is：")+str(b))