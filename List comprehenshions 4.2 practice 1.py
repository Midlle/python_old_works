left_boarder = int(input('Input A boarder: '))
right_boarder = int(input('Input B boarder: '))

square = [i ** 2 for i in range(left_boarder, right_boarder)]
cube = [i ** 3 for i in range(left_boarder, right_boarder)]

print(square)
print()
print(cube)
