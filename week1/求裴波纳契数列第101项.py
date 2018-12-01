a = 1
b = 1
for i in range(99):
    a,b = b,a + b
else:
    print(b)
