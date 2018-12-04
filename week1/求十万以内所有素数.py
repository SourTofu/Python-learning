n = 1275
flag = False
for i in range(2,n):
    if n % i == 0:
        flag = True
        print(i)
        break