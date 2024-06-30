def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [84, 'Карандаш', [15, 2, 11]]
values_dict = {'a': 99, 'b': 72.66, 'c': 'Ручка'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Циркуль', 33]
print_params(*values_list_2, 42)
