data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_args = 0


def calculate_structure_sum(*args):
    global sum_args
    for i in args:
        if type(i) == int:
            sum_args = sum_args + i
        elif type(i) == str:
            sum_args = sum_args + len(i)
        elif type(i) == dict:
            for key, value in i.items():
                sum_args = sum_args + len(key) + value
        else:
            for j in i:
                calculate_structure_sum(j)
    return sum_args


result = calculate_structure_sum(data_structure)
print(result)
