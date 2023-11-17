#1

class  Lecture1:
    #__init__ 메소드는 아래 4개의 인자를 가짐
    def __init__(self, name, which, room, professor):
        self.name=name
        self.which=which
        self.room=room
        self.professor=professor
        
    def study(self,major,what):
        #c의 print문은 아래와 같이 두 개의 인자를 출력해야 함
        print("%s의 %s을 공부할 것이다."%(self.name,what))
        
    def lecture(self,grade,major,name):
        #d의 print문은 학년, 전공, __init__메소드에 있는 강의이름을 출력해야함.
        print("%s %s 필수 과목은 %s이다."%(grade,major,self.name))
        
    def where(self,time):
        #e의 print문의 name,which,room은 위의 __init__메소드에 저장되어있기 때문에 self,time만 적음
        print("%s 강의는 %s %s에서 진행된다. (시작시간: %s)"%(self.name,self.which,self.room,time))
        
    def __add__(self,other):
        #f의 print문 %s에 들어갈 두 개의 name이 다르기 때문에 other이라는 인자 사용
        print("나는 %s과 %s를 수강하고 있다."%(self.name,other.name))
        
    def __sub__(self,other):
        #g의 print문 %s에 들어갈 두 개의 name이 다르기 때문에 other이라는 인자 사용
        print("오늘 %s과 %s은 모두 휴강이다."%(self.name,other.name))
        

class Lecture2(Lecture1):
    pass

#a
#객체의 이름이 noon이고 클래스 Lecture1을 사용. 강의명,강의건물,강의실,교수님을 차례로 입력
noon=Lecture1("프로그래밍입문","명신관","505호","김눈")

#b
#객체의 이름이 song이고 클래스 Lecture2를 사용. 강의명,강의건물,강의실,교수님을 차례로 입력
song=Lecture2("파이썬프로그래밍","새힘관","520호","김송")

#c
print("%s의 %s을 공부할 것이다."%(self.name,what))

#d
print("%s %s 필수 과목은 %s이다."%(grade,major,self.name))

#e
print("%s 강의는 %s %s에서 진행된다. (시작시간: %s)"%(self.name,self.which,self.room,time))

#f
print("나는 %s과 %s를 수강하고 있다."%(self.name,other.name))

#g
print("오늘 %s과 %s은 모두 휴강이다."%(self.name,other.name))

#h
#noon+song의 출력값은 __add__메소드를 이용해야 하기 때문에 아래와 같이 출력됨.
#프로그래밍입문과 파이썬프로그래밍을 수강하고 있다.

#i
#"파이썬프로그래밍과 프로그래밍입문은 모두 휴강이다." 출력코드
#메소드가 __sub__이기 때문에 '-'부호를 씀
song-noon

#j
#where메소드를 이용하여 "파이썬프로그래밍 강의는 새힘관 520호에서 진행된다. (시작시작: 1시 30분)"출력
#time만 __init__에 명시되어있지 않기 때문에 time만 넣음
song.where("1시 30분")
