#Task 1
# import random
#
# original_prices = [random.randint(-100, 100) for _ in range(10)]
#
#
# new_prices = original_prices[::]
#
# for i in range(len(original_prices)):
#
#     if new_prices[i] < 0:
#         new_prices[i] = 0
#
# print("Мы потеряли:", abs(sum(original_prices) - sum(new_prices)))
# #

#task 2
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print(nums[:6])
# print(nums[:-2])
# print(nums[::2])
# print(nums[::3])
# print(nums[::-1])
# print(nums[::-2])

#Task 3
import random

n = int(input("Введите количество чисел N: "))

numbers = [random.randint(-10, 10) for _ in range(n)]

a = random.randint(0, len(numbers) - 2)
b = random.randint(a + 1, len(numbers) - 1)
# Генерируем числа так, чтобы они не выходили за границу списка
print(numbers, a, b)
numbers = numbers[:a] + numbers[b + 1:]
print(numbers)