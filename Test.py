current = {}

while True:
    name = input('Name: ')
    phone = input('Phone number: ')
    current[name] = phone
    if name == 'stop' or phone == 'stop':
        print(f'current phonebook is {current}')
        break
    else:
        print(current)

