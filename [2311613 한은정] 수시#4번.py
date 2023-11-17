#프로그래밍 리포트 #연습 프로그래밍 02-3

#1번_[8,5,9,7] 순서대로 리스트에 넣기 위해 append를 이용해 차례대로 추가함.

mylist=[]
mylist.append(8)
mylist.append(5)
mylist.append(9)
mylist.append(7)

print(mylist)

#2번_'perls'를 먼저 빼기 위해 remove를 이용했고 리스트에 남은 'dot'의 앞에 'python'을 넣기 위해 맨 앞에 'python'이 들어간다는 뜻으로 insert를 씀.

mylist=['dot', 'perls']
mylist.remove('perls')
mylist.insert(0,'python')

print(mylist)

#3번_b를 print했을 때 456123이 나오기 위해서는 b와a를 합쳐야 함. 그래서 밑에 b=b+a라는 조건을 달아줌으로써 b는 456123이 들어간 리스트가 됨.
a=[1,2,3]
b=[4,5,6]
b=b+a

print(b)

#4번_1번과 같이 append를 이용해 순서대로 리스트에 동물들을 넣었고 len을 이용해 리스트에 있는 요소들의 개수를 셈으로써 3이 출력되게 함.
animals=[]
animals.append('cat')
animals.append('dog')
animals.append('mouse')
count=len(animals)

print(animals)
print(count)

#5번_처음엔 reverse를 이용해 순서를 반대로 정렬시켰고 두번째도 reverse를 이용해 이미 reverse된 리스트를 반대로 정렬시킴. 세번째는 전에 정렬됐던 리스트를 숫자 크기대로 정렬시키기 위해 sort를 씀.
mylist=[200,300,100,50]
mylist.reverse()
print(mylist)
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)

#6번_values안의 요소들의 각각 마지막 글자[-1]를 알파벳 순서대로 출력해서 ['bca', 'cab', 'abc']나옴. 출력된 리스트에서 [1]에 해당하는 문자는 각각 c,a,b순서이고 이를 알파벳 순으로 나열해서 ['cab', 'abc', 'bca']가 출력됨.
def lastchar(s):
    return s[-1]

values = ['abc', 'bca', 'cab']

values.sort(key=lastchar)
print(values)

values.sort(key=lambda s: s[1])
print(values)

#7번_맨 앞의 항을 지우기 위해 del names[0]을 이용했음. 다음에 나오는 Bill도 없애기 위해 [1]에 해당하는 요소를 지우는 del을 사용. 마지막으로 [0]에 해당하는 요소를 지우는 del을 이용해 Tommy를 제거함.
names=["Bill", "Tommy", "Bill", "Janet", "Stacy"]

del names[0]
print(names)

del names[1]
print(names)

del names[0]
print(names)


#8번_개수를 세는 함수인 count를 이용해 코드를 짬.
names=['a', 'a', 'b', 'c', 'a']
number=names.count('a')
print(number)

#9번
#Input list.
values=['uno', 'dos', 'tres', 'cuatro']

#Locate string._dos는 2번째 요소이므로 values[1]이고, 1에 대응하는 values는 dos이기 때문에 1 dos가 출력됨.
n=values.index('dos')
print(n,values[n])

#Locate another string._tres는 3번째 요소이므로 values[2]이고, 2에 대응하는 values는 tres이기 때문에 2 tres가 출력됨.
n=values.index('tres')
print(n,values[n])

#Handle nonexistent string._try에 실행할 코드를 넣고 except에 예외가 발생했을 때 처리하는 코드를 넣음. ?는 없기 때문에 except로 넘어가서 Not found가 출력됨.
try:
    n=values.index('?')
    #Not reached.
    print(n)
except:
    #Value not found.
    print("Not found")

#10번
#Create a list
elements=[]

#Append empty lists in first two indexes._elements에 리스트를 두 개 더 추가해 [[],[]]로 나옴.
elements.append([])
elements.append([])

#Add elements to empty lists._리스트 안의 리스트 중에 처음 리스트에 요소 1을 추가하고 같은 리스트에 요소 2를 추가함. [[1,2], []]로 나옴. 리스트 안의 리스트 중에 다음 리스트에 3을 추가한 후 4를 추가해 [[1,2],[3,4]]로 완성됨.
elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)

#Display top-left element._왼쪽의 [0]은 [1,2]를 말하고 오른쪽의 [0]은 [1,2]안의 1을 말함. 즉, 1이 출력됨.
print(elements[0][0])

#Display entire list._완성된 elements리스트를 출력하라는 뜻으로 [[1,2],[3,4]]로 출력됨.
print(elements)

#11번_v=mylist이므로 format에 의해 {v[0]}은10, {v[1]}은20, {v[2]}는30이 각각 들어감. str은 문자열을 출력하므로 결국 The values are 10, 20 and 30으로 출력됨.
mylist=[10,20,30]

res=str.format("The values are {v[0]}, {v[1]} and {v[2]}", v=mylist)
print(res)

#12번_all은 모든 요소가 참이면 true, 거짓이 하나라도 있으면 false가 나옴. any는 하나라도 참이 있으면 true를, 모든 요소가 거짓일 경우에만 false를 돌려줌.

#items에 하나라도 거짓이 있으면 False를 출력. 참이 1개 거짓이 2개 이므로 False가 나옴.
items=[False, None, True]
if not all(items):
    print(False)

#items에 모든 요소가 참이므로 true가 나옴.
items = [10,20,30]
if all(items):
    print(True)

#elements에 참이 하나 있으므로("Pomegranate") True가 나옴.
elements = [False, None, "Pomegranate", 0]
if any(elements):
    print(True)

#elements에 참이 없으므로 False가 나옴.
elements = [0,0,False]
if not any(elements):
    print(False)
