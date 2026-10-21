#2주차 p76 get_area

def get_area(radius):              #함수 출력
    area = 3.14 * radius**2
    return area

result = get_area(3)                    #함수 호출 -> 저장
print("반지름이 3인 원의 면적=", result)


#응용 제출
def get_area(width, height):
    area = width * height
    return area

result = get_area(5, 3)
print("사각형의 넓이 =", result)



#2주차 p46 중첩 반복문   

'''for y in range(5):
    for x in range(10):
        print("*",end="")
    print("")'''
>>>
**********
**********
**********
**********
**********


    
'''for y in range(4,0,-1):  #아니면 for y in range(1,5):
    for x in range(1,5):
        print("*",end="")
    print()'''
>>>
****
****
****
****


'''for i in range(1, 6):
    print("*" * i)'''

#별찍기(1->5) 제출

'''for i in range(1, 6):
    for j in range(i):
        print("*",end="")
    print()'''

#별찍기 (5->1) 제출
'''for i in range(5, 0, -1):
    for j in range(i):
        print("*",end="")
    print()'''



    
#continue
for i in range (10):
    if i % 3==0:
        continue
    else:
        print(i)
>>>
1
2
4
5
7
8


for i in range(1, 11):
    if i % 3 == 0:
        continue
    else:
        print(i)
    print("aaa")
>>>
1
aaa
2
aaa
4
aaa
5
aaa
7
aaa
8
aaa
10
aaa


for i in range (1,11):
    if i % 3==0:
        pass
    else:
        print(i)
    print("aaa")
>>>
1
aaa
2
aaa
aaa
4
aaa
5
aaa
aaa
7
aaa
8
aaa
aaa
10
aaa


for i in range (1,11):
    if i % 3==0:
        break
    else:
        print(i)
    print("aaa")
>>>
1
aaa
2
aaa



#입력&출력

'''def add(a,b):
    return a+b

a=10
b=20
add(10,20)
add(a,b)''' #아무것도 안나옴

'''def add(a,b):
    return a+b

a=10
b=20
print(add(10,20))
add(a,b)'''

#순서가 중요
'''def add(a,b):
    return a+b

c=10
d=20
print(add(10,20))
add(c,d)'''

'''def sub(): 
    pass'''   #함수 밑에 반드시 뭔가 써야함


#매개변수
'''def set_radius(radius):
    radius = 100
    return radius

r = 20
print(set_radius(r))

아니면
r=set_radius(r)
print(r)'''

#def add(a,b)


def printPattern(rows=5, cols=5, char="*"):
    pass

def printPattern(rows=5, char="A"):
    for _ in range(rows):
        for _ in range(5):
            print(char, end="")
        print()

printPattern()

def printPattern(rows=5, cols=5, char="*"):
    for _ in range(rows):
        for _ in range(cols):
            print(char, end="")
        print()

printPattern()
# 또는 다른 호출 예시:
# printPattern(3, 10)
# printPattern(3, 10, "%")

def printPattern(rows=3, char="*"):
    for _ in range(rows):
        for _ in range(5):
            print(char, end="")
        print()

printPattern()
>>>
*****
*****
*****
*****
*****

    
#제출 
'''def printPattern(rows=5, cols=5, char="*"):
    for _ in range(rows):
        for _ in range(cols):
            print(char, end="")
        print()

printPattern()



def printPattern(rows=5, cols=5, char="*"):
    for _ in range(rows):
        for _ in range(cols):
            print(char, end="")
        print()

printPattern(3, 10, "%")'''



'''def add (a,b=10,*numbers,):
    sum = 0
    
def add (*numbers,a): #a는 지역변수
    sum = 0'''


#tuple은 수정 불가능

'''def add (*numbers): 
    sum = 0
    for i in numbers:
        print(type(numbers))

print(add(10,20))'''

#가변인수로 합계 구하기 제출
def add (*numbers): 
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

print(add(10,20))


def add(a):
    return a + 10

print(add(10))  # 또는 print(add(a))

add2 = lambda x: x + 10

print(add2(10)

#전역변수
'''a=10

def add():
    a=20
    print(a)

add()
print(a)'''


#global
a=10

def add():
    global a   # 한줄로 global a=20은 오류남(대입연산자를 뒤에 쓸 수 없음)
    a=20
    print(a)

add()
print(a)

