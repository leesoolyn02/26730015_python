#python 300제 
#1 출력시 "', 구분하여 출력하기
print('신씨가 소리질렀다. "도둑이야"')

#2
print("Mary's cosmetics")

#3 priny(sep='')
print(1,2,3,4,5,6, sep='/')

#python 300제 07
print("naver", "kakao", "samsung", sep=";")
#naver;kakao;sk;samsung

#9 end="" 공백X, end=" " 공백O
for i in range(7):
    print(i,end="")
#print("first", end=""); print("second")

#13
s = "hello"
t = "python"
print(s+"!", t)
>>> hello! python

#type 값의 타입을 알려주는 함수
a=128
print(type(a)) #int

a="128"
print(type(a)) #str

a=12.5
print(type(a)) #float

# 문자(열) -> 정수 (str -> int)
a = "128"

# 변수에 대입해서 타입을 변경하지 않음
print(type(int(a)))

# 대입 해서 변수를 int 변경
a = int(a)

# 정수 -> 문자열
c = 123
c = str(c)

# 문자열 인덱싱 -> p t
letters = 'python'
print(letters[0], letters[2])

#문자열 슬라이싱 ->뒤에 4자리
license_plate = '24가 2210'
print(license_plate[-4::])

#문자열 슬라이싱 step
string = "홀짝홀짝홀짝"
print(string[::2]) #홀홀홀
print(string[1::2]) #짝짝짝

#문자열 슬라이싱 거꾸로 출력
srting = "PYTHON"
print(string[::-1])

#문자열 치환(replace())
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
# phone_number = phone_number.replace("-"," ")
print(phone_number)

#26
print(phone_number.replace("-"," "))

#27 split()-> 결과 리스트로 반환
url = "http://sharebook.kr" #kr
url= url.split('.')
print(url_split[-1])

#문자 + 문자 (더하기 연산 -> 연결)
a = "3"
b = "4"
print(a+b) #"34"

#문자 * 숫자 (곱하기-> 문자를 숫자만큼 반복해서 출력)
a = "hi"
print(a*10) # "hihihihihihihihihihi"


#35-37 검토

#문자열 곱하기 34번 문제 
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
#print((t1+' '+t2+' ')*4))

#35-37 검토

#38번 (콤마 제거 후 정수 형변환)
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))

#40번 strip()은 좌우 공백을 제거
data = "   삼성전자    "
print(data.strip())

# "2020-05-01"연도, 월, 일로 나눠보세요
date = "2020-05-01"
temp = data.split('-')
year=temp[0]
month=temp[1]
day=temp[2]
print(yeal)
print(month)
print(day)


#051 리스트 생성
movieas = ["닥터 스트레인지", "스플릿", "럭키"]

#리스트의 원소 추가 ->append('값')-맨 뒤에 값을 추가
movies = ["닥터 스트레인지", "스플릿", "럭키"]
movies.append("배트맨")
print(movies)

#53 리스트에 원소를 추가하는데 특정위치에 추가 insert()(인덱스,값)
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")

#54리스트 원소 삭제 (remove('값'),del리스트이름[인덱스],pop(인덱스)
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

movie_rank.remove('럭키')
del movie_rank[3]

#56리스ㅌ의 합(더하기 연산)*중복허용 
a=['a','b','c']
b=['a','b','c']
c=a+b

#57 리스트값중에 최대값(max()),최소값(min())
a_list=[1,2,3,4,5,6,7,8]
print(max(a_list))
print(min(a_list))

#58 리스트 요소값에 합 (sum())
print(sum(a_list))

#59 리스트 요소에 개수 (len())
print(len(a_list))

#60 리스트 요소값 평균 (sum()/len())
print(sum(a_list)/len(a_list))
