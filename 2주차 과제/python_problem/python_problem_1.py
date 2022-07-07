from itertools import count
from subprocess import call


num = 0

 
while True:

    try:
        call = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
    except:
        print('정수를 입력하세요')
    else:
        if call < 1 or call > 3:
            print('1,2,3 중 하나를 입력하세요')
        else:
            break
            