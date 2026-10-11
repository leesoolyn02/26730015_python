a = input()

for i in range(len(a)):
    if i == len(a) - 1:
        print(a[i])
    else:
        print(a[i], end=",")
