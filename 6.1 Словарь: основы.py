#
# phone_dic = {
#     'Vanya': 8999999999,
#     'Sveta': 7999999999,
#     'Pidrilkin': 699696969696
# }
#
# name = input('Input the name: ')
# if name in phone_dic:
#     print(phone_dic[name])
# else:
#     print('Error {0}'.format(name))

# task 2
student_str = input('Input studenst name with  space\n'
                    '(name, surname, city, university, marks: ')
student_info = student_str.split(' ')
student = dict()
student['Name'] = student_info[0]
student['Surname'] = student_info[1]
student['City'] = student_info[2]
student['University'] = student_info[3]
student['Marks'] = []

for i_grade in student_info[4:]:
    student['Marks'].append(i_grade)

for i_info in student:
    print(i_info, '-', student[i_info])
