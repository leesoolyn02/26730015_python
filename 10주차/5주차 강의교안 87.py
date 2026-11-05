#5주차 p87 세트의 연산 (코드제출)

#len()은 집합의 길이를 나타냄
fruits = {"apple", "banana", "grape"}
size = len(fruits)  # size는 3이 된다.
print(size)


#in 연산자를 사용하여 요소확인 
fruits = {"apple", "banana", "grape"}
if "apple" in fruits:
    print("집합 안에 apple이 있습니다.")
else:
    print("없습니다.")
    

#in 포함되는지
string = input()
fruits = {"apple", "banana", "grape"} #리스트나 튜플이여도 동일
if string in fruits:
    print( string,"있습니다.")
else:
    print(string,"없습니다.")
