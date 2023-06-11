word_1 = input('input sentence: ')
word_2 = input('input the second sentence: ')

word_1 = word_1.count('!') + word_1.count('?')
word_2 = word_2.count('!') + word_2.count('?')

if word_1 < word_2:
    word_1, word_2 = word_2, word_1

print(word_1 + word_2)
