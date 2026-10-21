for i in range(10):
    print(i,end=" ")
>>>0 1 2 3 4 5 6 7 8 9

for i in range(1,10,2):  #2칸씩
    print(i,end=" ") 
>>>1 3 5 7 9

for i in range(10,1,-2):  #10에서 거꾸로 2칸씩
    print(i,end=" ") 
>>>10 8 6 4 2

for _ in range(5):
    print("안녕하세요")


for i in range(1,101):        #실습1: 1부터 100까지의 수를 모두 출력하는 프로그램을 작성하시
        print(i,end = " ")


for i in range(10,-1,-1):  #10부터 0까지
    print(i,end=" ")'''
>>> 10 9 8 7 6 5 4 3 2 1 0 


#복합대입연산자

'''for i in [10,20,30,40]: #4번 반복과 동일
    a=[10,20,30,40] #이렇게 쓰면 리스트 재활용이 가능함 
for i in a :
    print(i,end=" ")'''

 

'''a=[10,20,30,40]  

#리스트 자체
for i in a :
    print(i,end=" ")

print("\n","-"*50)'''



#range
'''for i in range(len(a)) : 
    print(i,a[i],end =" ")  # 아니면 print(a[i],end =" ") '''
>>>0 10 1 20 2 30 3 40 아니면 10 20 30 40


'''for i in range(len(a)-1,-1,-1) : '''
    print(i,a[i],end =" ")
>>>3 40 2 30 1 20 0 10

'''for i in range(len(a)-1,-1,-1) : '''
    print(i,a[i])
3 40
2 30
1 20
0 10



i=1

while True:
    if i == 10:
        break
    print(i, end =" ")
    i+=1
>>>1 2 3 4 5 6 7 8 9



i = 0

while True:
    i += 1
    print(i, end=" ")
    
    if i >= 10:
        break
>>>1 2 3 4 5 6 7 8 9 10 



'''# 제어 변수를 선언한다.
i = 1
sum = 0

# i 값이 10보다 작으면 반복
while i <= 10:
    sum = sum + i
    i = i + 1

print("합계는", sum)'''





'''import random

tries = 0                       # 시도 횟수
guess = 0                       # 사용자의 추측값
answer = random.randint(1, 100) # 1과 100사이의 난수

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("너무 낮음!")
    elif guess > answer:
        print("너무 높음!")

if guess == answer:
    print("축하합니다. 시도횟수=", tries)
else:
    print("정답은 ", answer)'''


'''while True:
    if i%4==0 #나머지가 0인 특정 수의 배수 ex) 4의배수'''

#함수는 재활용하기 위해 사용, 함수는 순서가 중요하다, 내가 사용하기 전에 정의가 되어있어야함

#1부터 100까지 숫자 중 3의배수를 제외하고 출력
'''i=1
while True:
    if i >100:
        break
    if i%3==0:
        continue
    print(i,end=" ")
    i+=1
>>>1 2


def get_area(radius):    #정의
    area = 3.14*radius**2 
    return area

result = get_area(3) #호출
print("반지름이 3인 원의 면적=", result)'''


'''def sprint(a,b):
    return a+b

print(sprint(13,14))'''


# greet 함수

def greet(name, msg="파이썬"):
    print(name, msg)

greet("김한결","자바")


#다음주 람다, 지역 변수 ,전역 변수
