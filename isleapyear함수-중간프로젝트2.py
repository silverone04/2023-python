#중간프로젝트2번



def IsLeapYear(year):
        if ((year%4==0) and (year%100 !=0)) or (year%400==0):
            return True
        else:
            return False
            
while True:
    year=int(input())
    
    if year==0 or year<-1:
        print("잘못입력. 1이상 값 입력")

    elif year==-1:
        break
    
    else:
        if IsLeapYear(year):
                print("True")
        else:
                print("False")

