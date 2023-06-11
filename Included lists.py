n = int(input('hello'))
members = []
num = 1

for _ in range(n // 3):
    members.append(list(range(num, num + 3)))
    num += 3

print(members)

# words_in_text2

word_list = [['', 0], ['', 0], ['', 0]]

for i in range(3):
    word = input(f"Input the {i + 1} word: ")
    word_list[i][0] = word

text = input('Input the word from the text')
while text != 'end':
    for index in range(3):
        if word_list[index][0] == text:
            word_list[index][1] += 1
    text = input('Input the word from the text')

print('\nCounting the words from the text')

for i in range(3):
    print(word_list[i][0], ':', word_list[i])
