user_msg = input("Введите строку: ")
letters = list(user_msg)
what_replace = ":"
for_what_replace = ";"
index = 0
replace_count = 0

for letter in letters:
    if letter == what_replace:
        letters[index] = for_what_replace
        replace_count += 1
    index += 1

print("Исправленная строка:", end=' ')
for letter in letters:
    print(letter, end='')
