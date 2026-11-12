#1교시
#문자열 슬라이싱
#[start:end:step] -> end 생략하면 맨 끝까지 
#[:9] -> 0부터 시작
#[인덱스 번호]
'''
#[::] -> 전체 출력
s = 'Monty Python'
print(s[::]) # -> 0:12:1
>>>Monty Python

s = 'Monty 7724'
print(s[6:])
>>>7724

#뒤에서 네자리
s = 'Monty 안녕하세요 7724'
print(s[-4:]) #s[-4::]도 동일
              #어떤 문자열이 들어가도 뒤에서 4자리만 나옴
'''

'''
# 학생 정보가 담긴 문자열
student = "26730015이수린소프트웨어융합과"

# 문자열 슬라이싱으로 정보 추출
student_id = student[:8]    # 학번
name = student[8:11]        # 이름
major = student[11:]        # 학과

# 결과 출력
print("학번:", student_id)
print("이름:", name)
print("학과:", major)



# 기호| -> 이수린(3글자) 이수|(2글자) 이|(1글자)
student1 = "26730015이수|소프트웨어융합과"  
student2 = "26730015이|소프트웨어융합과"

pos = student1.find("|")
print(pos)

# 문자열 슬라이싱으로 정보 추출
student_id = student1[0:8]    # 학번
name = student1[8:pos]        # 이름
major = student1[11:]         #학과

print("학번:", student_id)
print("이름:", name)
print("학과:", major)

>>>학번: 26730015
이름: 이수
학과: 소프트웨어융합과
'''


''' 
student = "26730015이수린|소프트웨어융합과"

student_id = student1[0:8]    
name = student1[8:pos]        
major = student1[pos+1:]
'''

#구별하기
s = 'Monty Python'
print(s[-1])
print(s[:-1])
>>>
n
Monty Pytho

# 문자(열) 자료형 + 문자(열) 자료형 -> 연결
print("H" + "E")

# in, not in -> A in B -> A라는게 B에 존재하는지
#               A not in B -> A라는게 B에 존재하지 않는지
print("H" in "hello")
print("H" not in "hello")


# palindrome
a = "dad"
b = a[::-1]  # nohtyp

if a == b:
    print("Palindrome")
else:
    print("Not Palindrome")


#input()표준입력함수 (키보드->변수 저장)
response = input('게임을 계속하시겠어요?')

if response.lower() == 'yes' or 'y':
    print('게임을 계속합니다.')
else:
    print('다음에 또 봬요.')



'HELLO'.isupper()
True
'hello'.islower()
True
'abc'.isalpha()
True
'abc123'.isalpha()
False
'abc123'.isalnum()
True
'123'.isdecimal()
True
'\n'.isspace()
True

    

#10주차 p24
while True:
    password = input('새로운 패스워드를 선택하시오 (문자와 숫자만 가능): ')
    if password.isalnum():
        print("(정상)")
        break
    else:
        print('문자와 숫자만을 이용하여 패스워드를 선택하시오.')



# startswith(s) s로 시작하는지 검사
# endswith(s) s로 끝나는지 검사 (확장명 검사)


#split()->리스트 #기본값 공백 <=> string.split(' ')
string = 'welcome to python'
string = string,split() #원본 바꿈
print(string.split()) 
print(string)

string1 = "welcome/to/python"
string1 = string1.split('/')
print(string1)


#10주차 29p
#문자열을 하나의 문자 요소들로 변환 list()
string = 'welcome to python'
string = list(string)
print(string)

#문자열을 하나의 문자 요소들로 변환 list() 공백은 빼고
#replace(), join()
string1 = "welcome to python"
string1 = list(string1.replace(" ",""))
