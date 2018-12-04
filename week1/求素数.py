#count = 1
#for a in range(3,100000,2):
#    for i in range(2,a):
#        if a % i == 0:
#            break
#    else:
#        count +=1
#print(count)
n = 100000
p = [True] * (n + 1) # 为了方便使用n+1，使索引和数字对齐
p[0] = p[1] = False
for i in range(2, int(n ** 0.5 + 1.5)):
    if not p[i]:
        continue
    for j in range(i * i, n + 1, i): # 如果2是，则2的倍数都不是，因此，因此步长都是i。全部覆盖一遍
        p[j] = False
primes = [i for i in range(n + 1) if p[i]]

print(len(primes))