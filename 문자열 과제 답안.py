'''문자열 연습문제 1

#1 range 사용

a = input() 

for i in range(len(a)):
    print(a[i], end=" ") #a[i]는 변수

print()

#2.리스트 사용 (반복문으로 직접 접근)

a = input()

for i in a:
    print(i, end=" ") #list_append()

print()

#join 사용 구분자.join(문자열_반복가능객체)
a=input()

print(" ".join(a))

혹은

>>>print(" ".join("python"))
>>>p y t h o n'''


'''문자열 자가진단 1-1 


# 1. 슬라이싱

a = input()
print(*a[::2]) #print("a","c","e")  print("ace")    sep(" ")
이렇게 썼을때 왜 한칸씩 띄워지는지 이해만 할줄 알면됨

# enumerate() 사용 

s = input()

for i, c in enumerate(s):  #i는 인덱스 c는 값
    if i % 2 == 0:
        print(c, end=" ")

#보통 답안 
c=input()
for i in range(len(c)):
    ifi%2==0:
        print(c[i], end=" ")  #enumerate와의 차이점 c,c[i]'''



'''문자열 자가진단 1-2

# 1. 슬라이싱
s = input()
print(*s[::-1])

# 2. for() range()
s = input()

for i in range(len(s)-1, -1, -1):
    print(s[i], end="")

# 3. reversed()
s = input()

print(*reversed(s), sep="")'''


'''문자열 - 연습문제 2

print("""It's an apple.
He said "Hello!" to me""") #삼중 따옴표는 시험 안 나옴'''



'''문자열 - 연습문제 3

#1.split(' ') == split() #리스트로 저장됨
A = "apple orange banana" # 리스트 만들기,공백을 기준으로 나누어져있음
A = A.split()

print(A)
print(A[::-1]) #이렇게 하면 거꾸로 출력
B = " Hello world! "
print(B)
print(B.strip())

#양쪽 공백 제거 strip()
#왼쪽 공백 제거 lstrip()
#오른쪽 공백 제거 rstrip()


2.split('/')  #이건 지금 신경쓰지 말기
A = "apple/orange/banana"
A = A.split('/')
                       # 차이점: 각각의 구분을 뭘로 해놨느냐
print(A)

'''

'''문자열 - 자가진단 3

#공백으로 구분된 두개의 단어로 이루어진 문자열 입력
A,B= input().split()
print(B,A+B)

#:콜론으로 구분된 두개의 단어로 이루어진 문자열 입력
A,B= input().split(':')'''
#10:20


문자열 - 연습문제 5

#1. f-string
PI = 3.14
r = int(input())

area = r * r * PI

print(f"PI = {PI:.2f}")
print(f"Area = {r} * {r} * {PI} = {area:.1f}")

#2. format()
PI = 3.14
r = int(input())

area = r * r * PI

print("PI = {:.2f}".format(PI))
print("Area = {} * {} * {} = {:.1f}".format(r, r, PI, area))
