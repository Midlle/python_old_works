line = input('Input the line: ')
symbol = input('Symbol to add: ')

without_symbol = [letter * 2 for letter in line]
with_symblo = [i_letter * 2 + symbol for i_letter in line]

print(f'Список удвоенных символов: {without_symbol} \nСклейка с дополнительным символом: {with_symblo}')
