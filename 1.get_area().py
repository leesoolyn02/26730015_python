#2주차 p76 get_area

def get_area(radius):              #함수 출력
    area = 3.14 * radius**2
    return area

result = get_area(3)                    #함수 호출 -> 저장
print("반지름이 3인 원의 면적=", result)

#응용 
def get_area(width, height):
    area = width * height
    return area

result = get_area(5, 3)
print("사각형의 넓이 =", result)
