n = int(input())
result = 1
i = 1

while True:
    result = result * i
    if result >= n:
        print(i)
        break
    i = i + 1
