first = int(input('введите первое целое число: '))
second = int(input('введите второе целое число: '))
third = int(input('введите третье целое число: '))

if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
