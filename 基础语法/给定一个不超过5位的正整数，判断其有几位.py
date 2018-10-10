number = int(input('pless enter a number:'))
if number <= 0 :
    print('If the number is unqualified, the figure between 1-100000 should be entered.')
elif number < 10 :
    print('this is the one figure.')
elif number < 100 :
    print('this is the two figure.')
elif number < 1000 :
    print('this is the three figure.')
elif number < 10000 :
    print('this is the  four figure.')
elif number < 100000 :
    print('this is the five figure. ')
else:
    print('If the number is unqualified, the figure between 1-100000 should be entered. ')
#使用函数用法
#number = len(str(int(input('>>'))))
#print('this is the',number,'figure')