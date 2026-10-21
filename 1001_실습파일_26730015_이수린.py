#가변인수...람다함수...

'''#값을 하나 입력
a=input()

a=float(input())

a,b=input().split()
#공백을 기준으로 받음 예를 들어 10,10으로 입력
a,b=map(int,input().split())
#한줄에 여러개의 정수 값을 입력 받고 싶으면 map


#값을 하나 입력(정수)
a=int(input())'''


#지역변수&전역변수
'''gx = 100

def func1():
    print("func1() :", gx)

def func2():
    gx = 200
    print("func2() :", gx)

myfunc1()
myfunc2()
print("외부 :", gx)



gx = 100

def func1():
    global gx
    print("func1() :", gx)

func1()'''

#리스트

#append()는 맨 뒤에 추가됨-->요소 삭제하기 파트도 확인(pop,remove등)
'''fruits = []
fruits.append("apple")
fruits.append("banana")
print(fruits)'''

#내장함수는 자료형.함수로 작성



'''a = [5, 2, 1, 4, 6]

a.sort(reverse=False)  # 오름차순
print(a)

a.sort(reverse=True)   # 내림차순
print(a)'''




#문제 (첫 번째, 세 번째, 다섯 번째 점수를 순서대로 출력하는 프로그램)
'''score = [80, 90, 70, 100, 60]

for i in range(len(score)):
    if i % 2 == 0:
        print(score[i])'''

# 정수 n을 입력받고 n개의 점수를 입력받아 리스트에 저장한 후 리스트 전체를 출력하는 프로그램
'''N = int(input())
lst = []

for i in range(N):
    temp = int(input())
    lst.append(temp)

print(lst)'''

#0이 입력될 때까지 점수를 입력받아 리스트에 저장한 후 차례대로 출력하는 프로그램
lst = []

while True:
    n = int(input())

    if n == 0:
        break

    lst.append(n)

for i in lst:
    print(i)

#0이 입력될 때까지 정수를 입력받아 리스트에 저장한 후, 짝수번째(두 번째, 네 번째, 여섯 번째, ...) 값을 공백으로 구분하여 한 줄에 출력하는 프로그램
'''lst = []

while True:
    n = int(input())

    if n == 0:
        break

    lst.append(n)

for i in range(len(lst)):
    if i % 2 == 1:
        print(lst[i], end=' ')'''
