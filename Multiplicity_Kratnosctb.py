num_list = []
num_count = int(input('Insert count number = '))

for i in range(1, num_count + 1):
    ask_number = int(input(f"Insert {i} number: "))
    num_list.append(ask_number)

divider = int(input('Insert the divider: '))
index = 0
sum_indexes = 0

for i_index in num_list:
    if i_index % divider == 0:
        print("Индекс числа", i_index, ":", index)
        sum_indexes += index
    index += 1

print(f'Indexes summ {sum_indexes}')