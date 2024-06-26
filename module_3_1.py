calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(x):
    global calls
    count_calls()
    string = (len(x), x.upper(), x.lower())
    return string


def is_contains(y, z):
    global calls
    count_calls()
    string = y.upper()
    a = -1
    while a < len(z) - 1:
        a = a + 1
        list_to_search = z[a].upper()
        if string != list_to_search:
            continue
        else:
            return True
    a = -1
    while a < len(z) - 1:
        a = a + 1
        list_to_search = z[a].upper()
        if string == list_to_search:
            continue
        else:
            return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
