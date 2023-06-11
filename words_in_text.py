word_list = []
counts = [0, 0, 0]

for i in range(3):
    word = input(f"Input the {i + 1} word: ")
    word_list.append(word)

text = input('Input the word from the text')
while text != 'end':
    for index in range(3):
        if word_list[index] == text:
            counts[index] += 1
    text = input('Input the word from the text')

print('\nCounting the words from the text')

for i in range(3):
    print(word_list[i], ':', counts[i])
