# task 1
# number = int(input('Input number: '))
# num_dic = dict()
#
# for i in range(1, number + 1):
#     num_dic[i] = i ** 2
# print(num_dic)
#
# # task 2
# student_str = input('Input '
#                     'name, surname, city,university, marks with space: ').split(' ')
#
# student = dict()
# student['name'] = student_str[0]
# student['surname'] = student_str[1]
# student['city'] = student_str[2]
# student['university'] = student_str[3]
# student['marks'] = []
#
# for i_grades in student_str:
#     student['marks'].append(i_grades)
#
# for i in student:
#     print(i, '-', student[i])
current_contacts = {}
while True:
    print("Текущие контакты на телефоне:")
    if current_contacts:
        for name in current_contacts:
            print(name, current_contacts[name])
    else:
        print("<Пусто>")
    new_contact = input("Введите имя (для остановки введите пустую строку): ")
    new_telephone = int(input("Введите номер телефона: "))
    if new_contact in current_contacts:
        print("Ошибка: такое имя уже существует.")
    else:
        current_contacts[new_contact] = new_telephone
