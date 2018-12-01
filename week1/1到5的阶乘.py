#计算阶乘
while True:
    number = str(input("Pless Number:"))
    if number == "quit":
        break
    a = 1
    b = 0
    for i in range(1,int(number)+1):
        b = a * i
        a = b
    print(str(number)+" "+str("Factorial is：")+str(b))