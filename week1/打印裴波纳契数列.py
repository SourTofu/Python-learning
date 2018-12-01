a = 0
b = 1
for i in range(1,101):
     a,b = b,a+b
     if b > 100:
         break
     print(b)