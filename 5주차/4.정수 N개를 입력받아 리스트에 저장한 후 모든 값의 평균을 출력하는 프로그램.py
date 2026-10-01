N = int(input())
lst = []

for i in range(N):
    temp= int(input())
    lst.append(temp)

#방안1
avg = sum(lst) / N
print(int(avg))

#방안2
print(int(sum(lst(N)))

#방안3
total=0
    for i in lst:
        total+=i

print(int(total/len(lst)))
