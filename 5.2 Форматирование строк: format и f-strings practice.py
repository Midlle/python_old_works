# task 1
# name = input('name: ')
# order_number = input('order number: ')
#
# print('Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(
#     name,
#     order_number)
# )
# task 2 option 1
# name = input('Name: ')
# debt = int(input('Debt: '))
#
# print(f'{name}! {name}, привет! Как дела, {name}? Где мои {debt} рублей? {name}!' )
#  Task 2 option 2
# name = input('Name: ')
# debt = int(input('Debt: '))
#
# print('{name}! {name}, привет! Как дела, {name}? Где мои {debt} рублей? {name}!'.format(
#     name=name,
#     debt=debt)
# )
# Task 3
ip_adress = {'0', {'1'}, {'2'}, {'3'}}
num_list = []

for num in range(4):
    ip = int(input('Input number: '))
    if 0 < ip < 255:
        num_list.append(ip)
print(ip_adress.format(*num_list))

ip_address = "{0}.{1}.{2}.{3}"
count = 0# count otvechat za schet4ukom
numbers = []
while count < 4:
    new_number = int(input("Введите число: "))
    if 0 <= new_number <= 255:
        numbers.append(new_number)
        count += 1

print(ip_address.format(*numbers))
# * полезный инструмент, но и без него можно справиться, вручную прописав элементы по индексам
print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))
