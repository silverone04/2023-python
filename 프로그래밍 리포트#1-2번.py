#프로그래밍 리포트 #1_03-2

#a,b,c를 정수형으로 받기 위해 int사용
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

#정렬 전 a,b,c값 출력
print(a,b,c)

#if문을 이용해 크기 비교. a,b=b,a는 a,b값을 바꾼다는 의미, b,c=c,b는 b,c를 바꾼다는 의미
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
    
#오름차순 정렬된 a,b,c출력
print(a,b,c)
