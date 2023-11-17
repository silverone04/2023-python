from graphics import *
import re

# 그래프를 그리는 함수
def Draw(data):
    #창의 높이를 750으로 설정하면 보이지 않아서 660으로 수정
    win = GraphWin("Histogram", 1000, 660)
    win.setCoords(-1, -5, 15, 50)

    #그래프가 모두 포함되도록 하는 가로,세로 선
    #가독성을 위해 임의로 표시함
    x_axis = Line(Point(0,0), Point(20, 0))
    y_axis = Line(Point(0,0), Point(0, 50))
    x_axis.draw(win)
    y_axis.draw(win)

    #가로 축 숫자, 문자들
    labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "negative", "positive", "etc"]
    x = 0.5
    for label in labels:
        Text(Point(x, -1.5), label).draw(win)
        x += 1

    #세로 축 숫자들
    #0부터 100까지 5단위로 출력하되 그 간격은 2로 설정
    y = 0
    for label in range(0, 101, 5):
        Text(Point(-0.5, y), str(label)).draw(win)
        y += 2

    # 데이터에 따라 막대 그래프 그리기
    #0의 빈도수 좌측 상단의 x좌표가 0.3부터 시작하기 때문에 초깃값인 x를 0.3으로 설정
    x = 0.3
    a, b, c, d, e, f, final_result = 0, 0, 0, 0, 0, 0, 0
    x_sum=0
    y_sum=0
    for i in range(14):
        freq = data[i]
        
        #2단위의 높이를 5씩 기입했기 때문에 한 칸의 높이는 0.4
        
        height = freq * 0.4

        #final_result때문에 x좌표, y좌표 합 설정
        x_sum += x+ 0.4
        if height>=41:
            y_sum += 40
        else:
            y_sum += height

        #좌측 하단 좌표, 우측 상단 좌표 문자로 치환
        left_bottom=Point(x,0)
        right_top=Point(x+0.4, 40)

        
        #빈도수가 101 넘어갈 경우 막대를 y좌표 100에 맞춤
        if height>=41:
            bar = Rectangle(left_bottom, right_top)
            bar.setFill("green")
            bar.draw(win)
            
            #막대 위에 빈도수 표시
            Text(Point(x + 0.2, 41), str(freq)).draw(win)
            
        #빈도수가 100 이하인 경우
        else:
            bar=Rectangle(left_bottom, Point(x + 0.4, height))    
            bar.setFill('green')
            bar.draw(win)
            #막대 위에 빈도수 표시
            Text(Point(x + 0.2, height + 1), str(freq)).draw(win)
            
        x += 1

        #a
        if i == 3:
            a = height * 3.7
        #b
        elif i == 5:
            if height>=41:
                height=40
            b = height * 5.3
            
        #c    
        elif i == 8:
            c = height + 8.7
            
        #d
        elif i == 10:
            d = height + 10.3

        #e    
        e = data[11]

        #f
        f = data[12] * data[13]

        #final_result
        final_result=x_sum + y_sum
        
    win.getMouse()  #마우스 클릭으로 그래프 프로그램 종료
    win.close()

    return a,b,c,d,e,f,final_result

# 파일 내용 분석 및 그래프 작성
def analyze_file(file_name):
    frequencies = [0] * 14

    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            data = line.split()  #공백을 기준으로 데이터 분리
            
            for num_str in data:
                if num_str.isdigit():  #정수 처리
                    num=int(num_str)
                    if num == 0:
                        frequencies[0] += 1  # 0
                        
                    elif num == 1:
                        if num_str.startswith('0'):  #001처리
                            frequencies[13] += 1
                        else:
                            frequencies[1] += 1  # 1
                            
                    elif 0 < num <= 10:
                        frequencies[int(num)] += 1  # 2~10
                        
                    elif num >= 11:
                        frequencies[12] += 1  # 11 이상 positive
                        
                    elif num_str.startswith('-'):
                        frequencies[11] += 1 # 정수 음수
                        
                    else:
                        frequencies[13] += 1  # 그 외의 정수 etc
                            
                elif all(num_str.isdecimal() for num in data[1:]):
                    try:
                        num = float(num_str)  #float 처리
                        if num <0:
                            frequencies[11] += 1  # 음수 float
                        else:
                            frequencies[13] += 1  # 양수 float

                    except ValueError:
                        # 부동 소수점 숫자로 변환할 수 없는 경우 처리
                        frequencies[13] += 1  # 그 외의 정수

                elif num_str.startswith('-'):  #음수
                    if '.' in data[1:]:  #소수 중 음수
                        frequencies[11] += 1
                    elif data[1:].isdigit():
                        frequencies[11] += 1
                    else:
                        frequencies[13] += 1  #문자열
 
                else:
                    num=str(num_str)  #문자열
                    if num_str.startswith('0'):
                        frequencies[13] +=1
                    else:
                        frequencies[13] += 1 # 그 외

    return frequencies

            
# main 함수_파일 입력받는 함수
def main():
    file_name = input("Enter the file name: ")
    valid_file = False

    while not valid_file:
        try:
            frequencies = analyze_file(file_name)
            valid_file = True
        except FileNotFoundError:
            print("File not found. Please try again.")
            file_name = input("Enter the file name: ")

    a, b, c, d, e, f, final_result = Draw(frequencies)

    print(f"a: {a:.2f}")
    print(f"b: {b}")
    print(f"c: {c:.1f}")
    print(f"d: {d:.1f}")
    print(f"e: {e}")
    print(f"f: {f}")
    print(f"final_result: {final_result:.1f}")
    

if __name__ == "__main__":
    main()

