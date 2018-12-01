n = 10
e = n//2
for i in range(-e,n-e):
    prespace = -i if i < 0 else i
    print(' '*(e-prespace)+'*'*(2*prespace+1))
print()
for i in range(-5,6):
    if i >= 0:
        print(' '*(e-i)+'*'*(2*i+1))
    if i < 0:
        print(' '*(e+i)+'*'*(2*(-i)+1))
