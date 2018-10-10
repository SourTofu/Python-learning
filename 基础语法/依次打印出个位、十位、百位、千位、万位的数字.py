number1 = int(input('>>'))
number2 = len(str(number1))
print('this is the',number2,'figure')
number3 = number1
for i in range(number2):
    number4 = number3 // 10
    print(number3-number4*10)
    number3 = number4