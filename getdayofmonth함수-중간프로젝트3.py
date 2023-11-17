#중간프로젝트3

year=int(input("연도를 입력하세요: "))
month=int(input("월을 입력하세요: "))

def IsLeapYear(year):
    if ((year%4==0) and (year%100 !=0)) or (year%400==0):
        return 29
    else:
        return 28

def GetDayOfMonth(month):
    1<=month<=12
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    elif month==4 or month==6 or month==9 or month==11:
        return 30
    elif month==2:
        return IsLeapYear(year)

print(GetDayOfMonth(month))
