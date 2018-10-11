number1 = int(input('>>'))
number2 = len(str(number1))
print('this is the',number2,'figure')
number3 = number1
#for i in range(number2):
#    number4 = number3 // 10
#   print(number3-number4*10)
#  number3 = number4
#反序打印
pre = 0
for i in range(number2,0,-1):
    cur = number1//(10**(i-1))
    print(cur-pre*10)
    pre = cur
#思路：从各位依次打印万位
