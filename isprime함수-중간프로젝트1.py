#중간프로젝트1

def IsPrime(num):
    i=2
    while i<=num//2:
        if num%i==0:
            i+=1
            return 'False'
            break
        else:
            i+=1
            return 'True'

num=int(input())


while num!=-1:
    if num==2 or num==3:
        print('True')

    elif num<=1:
        print('잘못 입력하였습니다. 2이상의 값을 입력하여 주십시오.')
    else:
        a=IsPrime(num)
        print(a)
    num=int(input())
