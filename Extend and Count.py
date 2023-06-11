my_list = ['hello', 'command', 'option']
your_list = ['iphone', 'g7', 'etc']

my_list.extend(your_list)
print(my_list)
print()

pack = []
decode = []
bad_packs = 0

pack_amt = int(input('input the amout of packs: '))
for i_pack_num in range(pack_amt):
    print('\nPack num', i_pack_num + 1)
    for i_bit in range(4):
        print(i_bit + 1, 'bit', end=' ')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Lots of errors in pack')
        bad_packs += 1
    pack = []

print('\nincomming massege', decode)
print('errors in massege', decode.count(-1))
print('bad packs', bad_packs)
