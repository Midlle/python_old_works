word = input('Insert the word: ')
num_to_replace = int(input('number to replace: '))
what_to_replace = input('What do you want to replace: ')
world_list = []

world_list = list(word)
world_list[num_to_replace - 1] = what_to_replace

for i in world_list:
    print(i, end='')
