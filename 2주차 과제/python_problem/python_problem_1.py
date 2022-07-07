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
            
            

while(num<31):    
        i=0
        call=calling() 
        if i%2==0:
            for j in range(call):
                num=num+1
                print("PlayerA:",num)
                if num==31:
                    print("playerB win!")
                    break
        if i %2==1:
            for k in range(call):
                num=num+1
                print("PlayerB:",num)
                if num==31:
                    print("playerA win!")
                    break
        i=i+1