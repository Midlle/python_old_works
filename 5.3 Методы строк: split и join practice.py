# #task 1
# word_list = [input('Enter the word: ') for _ in range(3)]
# txt = input('input the text: ')
# word_count = [txt.count(word) for word in word_list]
#
# print(word_count)
#task 2
# text = input('Input the text: ')
# print(' '.join(text.split()))
#task 3
while True:
    grats = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
    if '{name}' in grats and '{age}' in grats:
        break
    else:
        print('Error')

surname_list = input('ФИ людей: ').split(', ')
age = input('Возраст каждого человека: ').split(' ')
ages = [int(i_number) for i_number in age]

for i_man in range(len(surname_list)):
    print(grats.format(name=surname_list[i_man], age=ages[i_man]))

people = [
    ' '.join([surname_list[i_man], str(ages[i_man])])
    for i_man in range(len(surname_list))]

people_str = ', '.join(people)
print('\n Birthdays ', people_str)
