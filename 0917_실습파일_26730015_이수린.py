#2주차 p76 get_area

'''def get_area(radius):
    area = 3.14 * radius**2
    return area

result = get_area(3)
print("반지름이 3인 원의 면적=", result)'''


#2주차 p46 중첩 반복문   #별 찍는거 시험 나옴

'''for y in range(5):
    for x in range(10):
        print("*",end="")
    print("")'''

for y in range(4,0,-1):
    for x in range(1,5):
        print("*",end="")
    print()
