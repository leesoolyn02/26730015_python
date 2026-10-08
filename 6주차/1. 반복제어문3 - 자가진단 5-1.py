#내가 쓴 답안
a, b = input().split()      #숫자-> 문자 chr()
                            #문자-> 숫자 ord()
a = ord(a)
b = ord(b)

if a <= b:
    for i in range(a, b + 1):
        print(chr(i), end=" ")
else:
    for i in range(a, b - 1, -1):
        print(chr(i), end=" ")


#답안
# 예제 1
a, b = input().split()

for i in range(ord(a),ord(b)+1):
        print(chr(i),end=" ")


# 예제 2
a, b = input().split()

if ord(a)< ord(b):
    for i in range(ord(a),ord(b)+1):
        print(chr(i),end=" ")
        
else:
    for i in range(ord(a),ord(b)-1,-1):
        print(chr(i),end=" ")


