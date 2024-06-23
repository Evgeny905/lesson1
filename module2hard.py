import random
def Pole_1():
    Number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    Win = random.choice(Number)
    return Win

Pole_1 = Pole_1()

Pole_2 = []

for i in range(1, Pole_1):
    for j in range(i, Pole_1):
        if Pole_1 % (i + j) == 0 and i != j:
            Pole_2.append(i)
            Pole_2.append(j)
            continue

Pole_2_Code = ''

for k in Pole_2:
    Pole_2_Code += str(k)


print('Камень в первом поле:', Pole_1)


print('Пароль:', Pole_2_Code)