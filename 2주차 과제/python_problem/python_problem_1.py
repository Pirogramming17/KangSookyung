from itertools import count
from subprocess import call
import random

num = 0

def calling():
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
    return call
            
            

    
for i in range(2):
    call=calling() 
    if i==0:
        for j in range(call):
            num=num+1
            print("PlayerA:",num)
    if i ==1:
        for k in range(call):
            num=num+1
            print("PlayerB:",num)
    