def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)


prices_now = [1.09, 23.56, 23, 4.56, 76]

first_percent = int(input('asdasd: '))
second_percent = int(input('MBNM: '))

prices_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
prices_second = [get_higher_price(second_percent, i_price) for i_price in prices_first]

print(f'sum for every year', round(sum(prices_now), 1), round(sum(prices_first), 1), round(sum(prices_second), 1))
