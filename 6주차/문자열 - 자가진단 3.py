a = input()

word1 = ""
word2 = ""
check = 0

for i in a:
    if i == " ":
        check = 1
    elif check == 0:
        word1 = word1 + i
    else:
        word2 = word2 + i

print(word2, word1 + word2)
