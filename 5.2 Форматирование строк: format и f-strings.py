while True:
    grats_template = input('Name {name}')
    if '{name}' in grats_template:
        break
    print('There;s no {name}')

names_list = []
print('Input names')
while True:
    name = input('')
    if name != 'end':
        names_list.append(name)
    else:
        break

for i_name in names_list:
    print(grats_template.format(name=i_name))

