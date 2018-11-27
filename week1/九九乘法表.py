for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+"x"+str(i)+"="+str(j*i)+'\t',end=' ')
    print()
print("")
for i in range(1,10):
    a = ''
    for j in range(i,10):
        a +=  '{}*{}={:<3}'.format(j,i,i*j)
    print("{:>70}".format(a))
#      print(str(i)+"x"+str(j)+"="+str(j*i)+'\t',end=' ')
