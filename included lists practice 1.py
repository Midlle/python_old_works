matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i_num in matrix:
    for iphone in i_num:
        print(iphone, end=' ')
    print()


n = int(input("Количество коньков: "))
skates = [int(input("Размер пары {}: ".format(i+1))) for i in range(n)]

k = int(input("Количество людей: "))
feet = [int(input("Размер ноги человека {}: ".format(i+1))) for i in range(k)]

skates.sort()
feet.sort()

i = j = count = 0
while i < n and j < k:
    if skates[i] <= feet[j]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1

print("Наибольшее количество людей, которые могут взять ролики:", count)