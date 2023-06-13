original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_prices = [(i_index if i_index > 0 else 0) for i_index in original_prices]

print(new_prices)


# 2 task
a = int(input('left: '))
b = int(input('right: '))

even = [x for x in range(a, b) if x % 2 == 0]

print(even)
