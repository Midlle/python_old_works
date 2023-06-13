import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
squad_3 = [('Dead' if squad_1[i_damage] + squad_2[i_damage] > 100
            else 'Alive')
           for i_damage in range(10)]

print('attack stat', squad_1, '\nattack stat', squad_2, '\nare they"re alive?', squad_3)
