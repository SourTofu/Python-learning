a = 7
for i in range(-a//2,a//2+1):
    if i >= 0:
        print(' '*i+'*'*(a-2*i))
    if i < 0:
        print(' '*(-i)+'*'*(a+2*i))