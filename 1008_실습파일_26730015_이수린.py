#5주차 강의교안 열람

'''
자료형.함수
(ex) list.append
a=[1,2,3,]
a.append(4)

a=[5,3,4,1,2]
a.sort() #기본값은 False,오름차순 정렬
print(a)

a=[5,3,4,1,2]
a.sort(reverse=True) #내림차순
print(a)
'''

''''
#sort 리스트.sort(reverse=False)
a.sort()
print(a)

#sorted sorted(리스트)
sorted()

#max,min,sum은 이터러블(iterable) 데이터(인덱스를 넣을 수 있는)를 넣을 수 있는 함수
'''



#아스키코드
'''
>>>a="hello"
>>>max(a)
'o'
혹은
>>>a="abcdf"
>>>max(a)
'f'
>>>ord('A')
65
>>>chr(66)
'B'

>>>for i in range(65,91):
        print(chr(i),end=" ")

   
>>>A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
'''


#1번
a, b = input().split()
#숫자-> 문자 chr()
#문자-> 숫자 ord()

a = ord(a)
b = ord(b)

if a <= b:
    for i in range(a, b + 1):
        print(chr(i), end=" ")
else:
    for i in range(a, b - 1, -1):
        print(chr(i), end=" ")

#비교연산자는 첫 번째 요소부터 비교  첫번째 요소가 같으면 주 번째 요소 부터 비교

#temps 중요
temps=[1,2,3,4]
values=temps #얕은 복사. 이부분이 중요.두개의 이름으로 한곳을 가리킴.독립적이지 않음

values=list(temps) #깊은 복사. 독립적


temps = [28, 31, 33, 35, 27, 26, 25]
values = temps

print("temps:", temps)
print("values:", values)

values.append("A")
print("values:", values)






a="Hello"
b=list(a)

#첫번째값
#print(a[0])
print(b)

a="Hello"
b=list(a)

c=[]

for i in a:
    c.append(i)

print(c)





#슬라이싱
a="Hello"
print(a[::])

#for i in range(시작값, 끝값, 단계)

#a[시작값:끝값:단계] #단계 기본값은 1



a = [10, 30, 20, 60, 50, 40]
a.sort()
del a[-1]        # del
a.remove(50)     # remove(값)
a.pop()          # pop(index)
print(a)

a = [10, 30, 20, 60, 50, 40]
a.sort(reverse=True)
del a[:3] # del
a.remove(50) # remove("값")
a.pop() # pop(index)
print(a)

#ell
print(a[1:4:1])

#olleH
print(a[::-1]) #거꾸로 출력


#license_plate= "24가 2210"  뒤에서 4자리만 출력

license_plate= "24가 2210"
print(license_plate[4::]) #2210이 출력되나 데이터가 바뀌면 다르게 출력
print(license_plate[-4::]) #이러면 데이터가 바뀌어도 뒤에서 4자리 출력 가능!


string = "홀짝홀짝홀짝"
print(str[::2])  #홀홀홀 출력
print(str[1::2])  #짝짝짝 출력


lang='python'
lang[0]='P'
print(lang) #문자열은 이터러블 데이터 중에 부분 수정 불가능 



del은 리스트 지울때 쓰는게 아니라 변수를 다루는 문법이다.


#리스트 함축

a = [i for i in range(100)]
print(a)




a = [i for i in range(1, 101) if i % 2 == 0]
print(a)




numbers = []

for x in range(100):
    if x % 2 == 0 and x % 3 == 0:
        numbers.append(x)


numbers = [x for x in range(1, 100) if x % 2 == 0 and x % 3 == 0]






a = [1, 2, 3, 4]  # 리스트
b = (1, 2, 3, 4)  # 튜플 read-only

print(sum(a[0:2]))
        
